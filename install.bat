@echo off
echo Fast-Phasr-Next————新一代轻量级Diffsinger自动音素标注工具

echo 请选择一个选项：
echo 1. 安装CPU版本
echo 2. 安装GPU版本

choice /c 12 /n

if %errorlevel% equ 1 (
    pip install -r requirement.txt
    echo 完成
) else if %errorlevel% equ 2 (
    conda install cudatoolkit -y
    pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
    pip install -r requirement.txt
        echo 完成
) else (
    echo 无效的选择
)