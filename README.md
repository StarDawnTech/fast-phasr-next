# Fast-Phasr-Next

<i>新一代轻量级Diffsinger音素自动标注工具</i>

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
python main.py -d [import directory] -m [model default="base"]
```