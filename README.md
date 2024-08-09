English | [简体中文](/README.zh-CN.md)

<div align="center">

<h1>Fast-Phasr-Next</h1>

<i>New generation lightweight DiffSinger automatic phoneme annotation tool</i>

<b>For a better solution,[please see here](https://github.com/wolfgitpr/LyricFA).</b>

<b>⚠️ Warning: Programs always have uncertainty, please do not trust automatic programs 100% (even if the program has high reliability). If it is a major project, please perform necessary checks on the phoneme sequence after using the program</b>

<b> Currently, the project supports Chinese, English, and Japanese (but the reliability of Japanese recognition is not high and a larger model needs to be selected)</b>

</div>

![](./img/workflow.png)

## Supported languages

- [x] Support for Chinese
- [x] Support for English
- [x] Support for Japanese

## Getting Started

### Requirements

```
torch
faster-whisper
pykakasi
```

fast-phasr-next requires Python 3.8 or later. We strongly recommend you create a virtual environment via Conda or venv before installing dependencies.

- install

```bash
# cpu
pip install -r requirement.txt

# gpu
conda install cudatoolkit -y
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118

pip install -r requirement.txt
```

### About Whisper

This project uses fast-whisper, which reimplements OpenAI's Whisper model using CTranslate2, a fast inference engine for the Transformer model. This implementation is 4x faster than openai/whisper but uses less memory and has the same accuracy. Efficiency can be further improved through 8-bit quantization on CPU and GPU.

In the test environment of RTX 3060 Laptop 6G GPU, using the Large-v3-fp16 model, it only takes about 0.7s to label a 6~10s audio, and in the labeling test of 50 audios, about 98.71% can be obtained accuracy

#### Optional model

|  Size  | Parameters | English-only model | Multilingual model | Required VRAM | Relative speed (Compared with the original project) |
| :----: | :--------: | :----------------: | :----------------: | :-----------: | :------------: |
|  tiny  |    39 M    |     `tiny.en`      |       `tiny`       |     ~1 GB     |      ~128x     |
|  base  |    74 M    |     `base.en`      |       `base`       |     ~1 GB     |      ~64x      |
|  small |   244 M    |     `small.en`     |      `small`       |     ~2 GB     |      ~36x      |
| medium |   769 M    |    `medium.en`     |      `medium`      |     ~5 GB     |      ~8x       |
| large  |   1550 M   |        N/A         |      `large`       |    ~10 GB     |      ~4x       |

### Inference

```
python main.py -d [import directory] -m [model default="large"] -l [language default="Chinese"] --device [default="cuda"] --compute_type [default="float16"]
```

## Thank you to the following contributors!

<a href="https://github.com/StarDawn-VirtualSinger/fast-phasr-next/contributors">
  <img src="https://contrib.rocks/image?repo=StarDawn-VirtualSinger/fast-phasr-next" />
</a>