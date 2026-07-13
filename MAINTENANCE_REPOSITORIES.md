# Maintenance repositories

本改造由以下四个仓库共同维护：

| 仓库 | 构建角色 | 本次是否包含源码提交 |
|---|---|---|
| [iptvorganization/TV](https://github.com/iptvorganization/TV/tree/fongmi) | Android 应用、Leanback/Mobile UI、实时语音字幕与翻译、播放器接线 | 是，`fongmi` 分支 |
| [iptvorganization/media](https://github.com/iptvorganization/media/tree/codec-support) | Media3 AV3A decoder、Dolby Vision、HEVC-FLV、轨道选择修复 | 是，`codec-support` 分支 |
| [iptvorganization/VividLib](https://github.com/iptvorganization/VividLib) | `libav3aJNI.so` 的 AVS3/AV3A 解码器源码 | 否；固定复用提交 `10a5c7140a15f179a7d94fbff76f9176063f7a97` |
| [iptvorganization/sherpa-onnx](https://github.com/iptvorganization/sherpa-onnx) | 本地多语种流式 ASR runtime 的后续维护入口 | 否；应用当前集成 sherpa-onnx v1.13.4 runtime |

## Checkout layout

```text
parent/
├── FongMi-TV/       # iptvorganization/TV
├── FongMi-media/    # iptvorganization/media
└── refs/
    └── VividLib/    # iptvorganization/VividLib（仅在重建 AV3A so 时需要）
```

日常编译 APK 必须同时检出 `TV` 的 `fongmi` 分支与 `media` 的 `codec-support` 分支。只有重建 `libav3aJNI.so` 时才需要检出 `VividLib`；正常 APK 编译会直接使用仓库中已构建的两个 ABI so。`sherpa-onnx` 无需作为 Gradle composite checkout，应用使用 `app/libs` 与 `app/src/main/jniLibs` 中固定版本的 runtime，语言模型按需下载。

应用基准版本由根目录 [`version.properties`](version.properties) 统一维护。功能版本更新时同时递增 `VERSION_CODE` 并更新语义化 `VERSION_NAME`；公开自动构建通过 Gradle 属性生成单调递增且可追溯的 CI 版本，不直接改写源码。完整规则见 [`VERSIONING.md`](VERSIONING.md)。
