# On-demand ASR model sources

The application does not bundle ASR weights. A language selection deterministically downloads one language package, verifies every file by exact byte length and SHA-256, and stores it in a separate removable directory.

| UI language | Runtime package | Upstream model |
|---|---|---|
| 普通话 | Streaming Zipformer2 CTC INT8 | [csukuangfj/sherpa-onnx-streaming-zipformer-ctc-zh-int8-2025-06-30](https://huggingface.co/csukuangfj/sherpa-onnx-streaming-zipformer-ctc-zh-int8-2025-06-30) |
| 粤语 | WenetSpeech Yue U2++ CTC INT8 | [csukuangfj/sherpa-onnx-wenetspeech-yue-u2pp-conformer-ctc-zh-en-cantonese-int8-2025-09-10](https://huggingface.co/csukuangfj/sherpa-onnx-wenetspeech-yue-u2pp-conformer-ctc-zh-en-cantonese-int8-2025-09-10) |
| 德语 | Kroko streaming Zipformer | [csukuangfj/sherpa-onnx-streaming-zipformer-de-kroko-2025-08-06](https://huggingface.co/csukuangfj/sherpa-onnx-streaming-zipformer-de-kroko-2025-08-06) |
| 英语 | Kroko streaming Zipformer | [csukuangfj/sherpa-onnx-streaming-zipformer-en-kroko-2025-08-06](https://huggingface.co/csukuangfj/sherpa-onnx-streaming-zipformer-en-kroko-2025-08-06) |
| 法语 | Kroko streaming Zipformer | [csukuangfj/sherpa-onnx-streaming-zipformer-fr-kroko-2025-08-06](https://huggingface.co/csukuangfj/sherpa-onnx-streaming-zipformer-fr-kroko-2025-08-06) |
| 西班牙语 | Kroko streaming Zipformer | [csukuangfj/sherpa-onnx-streaming-zipformer-es-kroko-2025-08-06](https://huggingface.co/csukuangfj/sherpa-onnx-streaming-zipformer-es-kroko-2025-08-06) |
| 日语 | Moonshine v2 Tiny quantized | [csukuangfj2/sherpa-onnx-moonshine-tiny-ja-quantized-2026-02-27](https://huggingface.co/csukuangfj2/sherpa-onnx-moonshine-tiny-ja-quantized-2026-02-27) |

The four Kroko community packages point to [Banafo/Kroko-ASR](https://huggingface.co/Banafo/Kroko-ASR) for model licensing (CC-BY-SA community weights). The inference engine remains the single sherpa-onnx runtime already used by the app; selecting another language does not install another FFmpeg or JNI engine.
