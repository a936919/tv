# AV3A、Dolby Vision 与 HEVC-FLV 源码构建

本分支将 TV 直接连接到 FongMi 的 Media3 fork，并启用以下播放链路：

- MPEG-TS/HLS `stream_type=0xD5` AV3A：同步头解析、轨道 Format、FFmpeg `libarcdav3a` 解码器选择，以及 Android 12L 以下 10 声道到 5.1 bed 的兼容映射。
- MPEG-TS/HLS Dolby Vision：解析 PMT `0xB0` Dolby Vision descriptor，在 H.265 reader 输出 `video/dolby-vision` 与 `dvhe` CSD。
- HEVC-FLV：兼容传统 codec id `12`，并支持 Enhanced RTMP v2 `hvc1` 的 `SequenceStart`、`CodedFrames` 和 `CodedFramesX`。

## 目录布局

```text
parent/
├── FongMi-TV/       # 本仓库
└── FongMi-media/    # iptvorganization/media 的 codec-support 分支
```

也可以用 `-PandroidxMediaDir=/absolute/path/to/media` 指定 Media3 fork。

```bash
git clone --branch fongmi https://github.com/iptvorganization/TV.git FongMi-TV
git clone --branch codec-support https://github.com/iptvorganization/media.git FongMi-media
```

AV3A native decoder 不再复用 JADX 参考 APK 的预编译库。`tools/build-av3a-from-source.sh` 默认从维护仓库 [iptvorganization/VividLib](https://github.com/iptvorganization/VividLib) 的固定提交 `10a5c7140a15f179a7d94fbff76f9176063f7a97` 构建；其上游是 [mytv-android/VividLib](https://github.com/mytv-android/VividLib)，并与 [nilaoda/Sourcecodeforplayer](https://github.com/nilaoda/Sourcecodeforplayer) 同源，VividLib 额外包含 arm64 构建支持。

构建输出是两个 ABI 各一个自包含的 `libav3aJNI.so`：只包含 AVS3 decoder、内置神经网络模型和很薄的 Media3 JNI bridge，**不编译、不链接、不加载 VividLib 的 FFmpeg**，也不包含此次不需要的 binaural renderer。独立 `media3-lib-decoder-av3a` renderer 只声明支持 `audio/av3a`；AAC、AC3、E-AC3、DTS 等普通音轨继续走应用原有的 MediaCodec/扩展 renderer，不受 AV3A 库影响。

`libav3aJNI.so` 不依赖参考 APK 的 `libAVS3AudioDec.so`、`libav3a_binaural_render.so`、`libffmpegJNI.so` 或 `libc++_shared.so`。支持：

- `arm64-v8a`：mobile 与 64 位电视。
- `armeabi-v7a`：Sony 等 32 位电视。

AV3A 与 AAC 同时存在时，默认明确优先 AV3A，避免 HLS 刷新时在 5.1 与立体声之间抖动；设置中开启“优先 AAC”后仍优先 AAC。已选中的任意音频或视频轨再次点击为幂等操作，不会生成空 override 或重复拆建 decoder。字幕轨仍保留再次点击关闭的行为。

## Dolby Vision Profile 覆盖

JADX 参考应用的 `DolbyVisionConfig` 只接受 Profile `4/5/7/8/9/10`，本分支与其逐项一致：

| Profile | codec string | 基础编码 | 支持范围 |
| --- | --- | --- | --- |
| 4 | `dvhe.04.xx` | HEVC | 配置解析、MP4/fMP4、HEVC TS/HLS 单 ES |
| 5 | `dvhe.05.xx` | HEVC | 同上；额外补齐 BT.2020 + ST2084 + limited range，避免绿/紫画面 |
| 7 | `dvhe.07.xx` | HEVC | 同上；“DV7回退”现在真正控制无 DV decoder 时的可选 HEVC base-layer 回退 |
| 8 | `dvhe.08.xx` | HEVC | 同上；已在 Sony 真机以 `dvhe.08.09` 点亮 Dolby Vision |
| 9 | `dvav.09.xx` | AVC | 配置解析、MP4/fMP4 与 AVC decoder 选择/回退 |
| 10 | `dav1.10.xx` | AV1 | 配置解析、MP4/fMP4 与 AV1 decoder 选择/受限回退 |

Profile `0/1/2/3/6` 与 `11+` 和参考应用一样不接受。MPEG-TS 的 PMT `0xB0` 直播接线属于 HEVC reader，所以针对 Profile `4/5/7/8`；Profile `9/10` 走 AVC/AV1 的 MP4/fMP4 路径。若双层流把 BL 与 EL 放在不同 dependency PID，本分支和参考应用都没有做跨 PID 合层；同一 ES 内交给硬件 DV decoder 的 NAL/RPU 会原样保留。

## 验证

```bash
export JAVA_HOME=/path/to/jdk-21
export ANDROID_HOME=$HOME/Library/Android/sdk

# 从固定源码提交只构建 AV3A JNI，并写入两个 ABI 的 jniLibs。
cd FongMi-TV
VIVID_SOURCE_DIR=../refs/VividLib \
  MEDIA3_DIR=../FongMi-media \
  tools/build-av3a-from-source.sh

# 或显式指定 VividLib 维护 fork（默认值已是该地址）。
VIVID_REPOSITORY=https://github.com/iptvorganization/VividLib.git \
  VIVID_COMMIT=10a5c7140a15f179a7d94fbff76f9176063f7a97 \
  MEDIA3_DIR=../FongMi-media \
  tools/build-av3a-from-source.sh

cd ../FongMi-media
./gradlew \
  :lib-extractor:testDebugUnitTest \
  --tests androidx.media3.extractor.flv.VideoTagPayloadReaderTest \
  --tests androidx.media3.extractor.ts.Av3aReaderTest \
  --tests androidx.media3.extractor.ts.DolbyVisionDescriptorTest \
  :lib-exoplayer:testDebugUnitTest \
  --tests androidx.media3.exoplayer.video.MediaCodecVideoRendererTest.supportsFormat_profile7HevcFallback_isOptIn \
  :lib-decoder-ffmpeg:testDebugUnitTest \
  --tests androidx.media3.decoder.ffmpeg.FfmpegLibraryTest

cd ../FongMi-TV
./gradlew :app:assembleLeanbackArmeabi_v7aDebug
./gradlew :app:assembleMobileArm64_v8aDebug
```

输出：

- `app/build/outputs/apk/leanbackArmeabi_v7a/debug/app-leanback-armeabi_v7a-debug.apk`
- `app/build/outputs/apk/mobileArm64_v8a/debug/app-mobile-arm64_v8a-debug.apk`

源码构建对 VividLib 做两个最小 Android 适配：使用 `model.h` 已内嵌的神经模型而不是尝试打开不存在的 `./bin/model.bin`；兼容新版 Clang 同时定义 `linux` 与 `aarch64` 的情况。脚本对补丁上下文和源码 commit 都做严格校验，源码变化时会直接停止而不是静默产出错误库。Dolby Vision 与 HEVC-FLV 仍是 Media3 extractor/video renderer 的 Java 源码改造，和独立 AV3A `.so` 没有链接关系，也没有被此构建脚本改动。

## 参考流

- AV3A：`http://82.156.243.185:36888/av3a/cctv16.m3u8`
- AV3A 10ch/5.1.4：`http://192.168.10.1:38766/cctv8k.m3u8`
- AV3A 标记 5.1.4、有效 6ch bed：`http://192.168.10.1:38766/cctv4k.m3u8`
- Dolby Vision：`https://cdn.staticres.top/p/b1ea7ad7-d641-4c00-8b52-185c98fb9190`

源码构建未包含上游发布流程中忽略的 MPV Media3 AAR 与 `DiskPreloadManager` AAR；`app/src/codecFallback` 让这两个可选功能回退到 Exo/无预缓存，不影响本次三种格式的内置 Exo 播放链路。
