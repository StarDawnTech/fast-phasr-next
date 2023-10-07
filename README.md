<div align="center">

<h1>Fast-Phasr-Next</h1>

<i>新一代轻量级 DiffSinger 自动音素标注工具</i>

<b>⚠️ 警告：程序永远存在不确定性，请不要 100%相信自动程序（即使程序有很高的可靠性），如果是重大项目请在使用该程序后对音素序列进行必要的检查</b>

<b> 目前，本项目仅支持中文和英文 </b>

</div>

## 使用

### 依赖

```
torch
openai-whisper
pypinyin
ffmpeg
```
**请自行安装ffmpeg并添加到系统环境变量**

### 安装依赖

```bash
git clone https://github.com/StarDawn-VirtualSinger/fast-phasr-next.git
```

- 创建 conda 环境

```
conda create -n fast-phasr-next python==3.12 -y
conda activate fast-phasr-next
```

- 使用脚本：

```bash
# windows
.\install.bat

# linux
bash ./install.sh
```

- 手动安装

```bash
# cpu
pip install -r requirement.txt

# gpu
conda install cudatoolkit -y
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118

pip install -r requirement.txt
```

### 可选模型

|  Size  | Parameters | English-only model | Multilingual model | Required VRAM | Relative speed |
| :----: | :--------: | :----------------: | :----------------: | :-----------: | :------------: |
|  tiny  |    39 M    |     `tiny.en`      |       `tiny`       |     ~1 GB     |      ~32x      |
|  base  |    74 M    |     `base.en`      |       `base`       |     ~1 GB     |      ~16x      |
| small  |   244 M    |     `small.en`     |      `small`       |     ~2 GB     |      ~6x       |
| medium |   769 M    |    `medium.en`     |      `medium`      |     ~5 GB     |      ~2x       |
| large  |   1550 M   |        N/A         |      `large`       |    ~10 GB     |       1x       |

**实际测试中，base 和 small 模型已经能取得较好的标注效果，非必要无需选择更大的模型**

### 推理

```
python main.py -d [import directory] -m [model default="base"] -l [language default="auto"]
```

## 感谢以下贡献者！

<a href="https://github.com/StarDawn-VirtualSinger/fast-phasr-next/contributors">
  <img src="https://contrib.rocks/image?repo=StarDawn-VirtualSinger/fast-phasr-next" />
</a>
