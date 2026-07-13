#!/usr/bin/env bash
set -euo pipefail

ROOT=$(cd "$(dirname "$0")/.." && pwd)
MEDIA3_DIR=${MEDIA3_DIR:-"$ROOT/../FongMi-media"}
VIVID_SOURCE_DIR=${VIVID_SOURCE_DIR:-}
BUILD_DIR=${BUILD_DIR:-"$ROOT/app/build/av3a-native"}
NDK=${NDK:-"${ANDROID_NDK_HOME:-$HOME/Library/Android/sdk/ndk/28.2.13676358}"}
VIVID_REPOSITORY=${VIVID_REPOSITORY:-https://github.com/iptvorganization/VividLib.git}
VIVID_COMMIT=${VIVID_COMMIT:-10a5c7140a15f179a7d94fbff76f9176063f7a97}
ABIS=(arm64-v8a armeabi-v7a)

case "$(uname -s)" in
    Darwin) NDK_HOST=darwin-x86_64 ;;
    Linux) NDK_HOST=linux-x86_64 ;;
    *) echo "Unsupported build host: $(uname -s)" >&2; exit 1 ;;
esac

TOOLCHAIN="$NDK/toolchains/llvm/prebuilt/$NDK_HOST/bin"
CMAKE=${CMAKE:-$(command -v cmake)}
NINJA=${NINJA:-$(command -v ninja)}
STRIP="$TOOLCHAIN/llvm-strip"

test -x "$TOOLCHAIN/clang"
test -f "$MEDIA3_DIR/libraries/decoder_av3a/src/main/jni/av3a_jni.cc"
rm -rf "$BUILD_DIR"
mkdir -p "$BUILD_DIR"

if [[ -z "$VIVID_SOURCE_DIR" ]]; then
    git clone --filter=blob:none "$VIVID_REPOSITORY" "$BUILD_DIR/VividLib"
    git -C "$BUILD_DIR/VividLib" checkout --detach "$VIVID_COMMIT"
    VIVID_SOURCE_DIR="$BUILD_DIR/VividLib"
else
    VIVID_SOURCE_DIR=$(cd "$VIVID_SOURCE_DIR" && pwd)
fi

ACTUAL_COMMIT=$(git -C "$VIVID_SOURCE_DIR" rev-parse HEAD)
if [[ "$ACTUAL_COMMIT" != "$VIVID_COMMIT" ]]; then
    echo "VividLib must be pinned to $VIVID_COMMIT (got $ACTUAL_COMMIT)" >&2
    exit 1
fi

# Only the AVS3 decoder sources are copied. VividLib's FFmpeg tree and binaural
# renderer are deliberately excluded from this build.
cp -R "$VIVID_SOURCE_DIR/av3adecoder" "$BUILD_DIR/av3adecoder"

python3 - "$BUILD_DIR" <<'PY'
from pathlib import Path
import sys

root = Path(sys.argv[1]) / "av3adecoder"
init = root / "avs3Decoder/src/avs3_init_dec.c"
text = init.read_text()
old = '''    hAvs3Dec->modelType = HYPER;
    if ((*fModel = fopen(modelPath, "rb")) == NULL)
    {
        LOGD("Can not open model file. modelpath: %s\\n", modelPath);
        fprintf(stderr, "Can not open model file.\\n");
        return -1;
    }
    LOGD("The model file loaded successfully.\\n");
'''
new = '''    hAvs3Dec->modelType = HYPER;
    /* The neural model is embedded in model.h. Android has no ./bin/model.bin. */
    (void)modelPath;
    *fModel = NULL;
    LOGD("Using embedded AVS3 neural model.\\n");
'''
if old not in text:
    raise SystemExit("VividLib embedded-model patch context changed")
init.write_text(text.replace(old, new))

decoder = root / "avs3Decoder/src/decoder.c"
text = decoder.read_text()
old = '''\t\tAvs3InitDecoder(hAvs3Dec, &hAvs3Dec->fModel, "./bin/model.bin");
//\t\tprintf("Avs3InitDecoder out\\n");
\t\thAvs3Dec->bInited = 1;
'''
new = '''\t\tif (Avs3InitDecoder(hAvs3Dec, &hAvs3Dec->fModel, NULL) != 0)
\t\t\treturn AVS3_FALSE;
//\t\tprintf("Avs3InitDecoder out\\n");
\t\thAvs3Dec->bInited = 1;
'''
if old not in text:
    raise SystemExit("VividLib decoder init patch context changed")
decoder.write_text(text.replace(old, new))

version = root / "avs3Decoder/include/Version.h"
text = version.read_text()
old = "#ifdef linux\n"
new = "#if defined(linux) && !defined(ARCH_AARCH64)\n"
if text.count(old) != 1:
    raise SystemExit("VividLib Version.h patch context changed")
version.write_text(text.replace(old, new))
PY

for ABI in "${ABIS[@]}"; do
    NATIVE_BUILD="$BUILD_DIR/cmake-$ABI"
    "$CMAKE" -S "$ROOT/tools/av3a-native" -B "$NATIVE_BUILD" -G Ninja \
        -DCMAKE_MAKE_PROGRAM="$NINJA" \
        -DCMAKE_TOOLCHAIN_FILE="$NDK/build/cmake/android.toolchain.cmake" \
        -DANDROID_ABI="$ABI" -DANDROID_PLATFORM=android-24 \
        -DANDROID_STL=c++_static -DCMAKE_BUILD_TYPE=Release \
        -DVIVID_DIR="$BUILD_DIR" -DMEDIA3_DIR="$MEDIA3_DIR"
    "$CMAKE" --build "$NATIVE_BUILD" --parallel
    "$STRIP" --strip-unneeded "$NATIVE_BUILD/libav3aJNI.so"

    DEST="$ROOT/app/src/main/jniLibs/$ABI"
    # AV3A and sherpa-onnx intentionally share the app ABI directory. Rebuilding
    # one native component must not delete the other component's JNI runtime.
    mkdir -p "$DEST"
    rm -f "$DEST/libav3aJNI.so"
    install -m 755 "$NATIVE_BUILD/libav3aJNI.so" "$DEST/libav3aJNI.so"
done

for ABI in "${ABIS[@]}"; do
    test -s "$ROOT/app/src/main/jniLibs/$ABI/libav3aJNI.so"
done

{
    echo "VividLib source: $VIVID_REPOSITORY"
    echo "VividLib commit: $VIVID_COMMIT"
    echo "Native design: direct AVS3 decoder; no FFmpeg; no binaural renderer"
    echo "NDK: $NDK"
    sha256sum "$ROOT"/app/src/main/jniLibs/*/libav3aJNI.so
} | tee "$BUILD_DIR/provenance.txt"
