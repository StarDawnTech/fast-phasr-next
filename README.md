# Fast-Phasr-Next

<i>新一代轻量级Diffsinger自动音素标注工具</i>

**目前仅支持中文**

## 使用

### 依赖

```
torch
openai-whisper
pypinyin
```

### 安装依赖

```
# cpu
pip -r requirement.txt

# gpu
conda install cudatoolkit -y
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118

pip -r requirement.txt
```

### 推理

```
python main.py -d [import directory] -m [model default="base" -l [language default="auto"]]
```

可选模型

|  Size  | Parameters | English-only model | Multilingual model | Required VRAM | Relative speed |
|:------:|:----------:|:------------------:|:------------------:|:-------------:|:--------------:|
|  tiny  |    39 M    |     `tiny.en`      |       `tiny`       |     ~1 GB     |      ~32x      |
|  base  |    74 M    |     `base.en`      |       `base`       |     ~1 GB     |      ~16x      |
| small  |   244 M    |     `small.en`     |      `small`       |     ~2 GB     |      ~6x       |
| medium |   769 M    |    `medium.en`     |      `medium`      |     ~5 GB     |      ~2x       |
| large  |   1550 M   |        N/A         |      `large`       |    ~10 GB     |       1x       |
