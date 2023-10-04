@echo off
echo Fast-Phasr-Next————新一代轻量级Diffsinger自动音素标注工具
echo 十分推荐您创建一个Conda环境！Conda环境就像冰箱里的盒子一样保证不串味！

echo 请选择一个选项：
echo 1. 安装CPU版本
echo 2. 安装GPU版本
echo 3. 创建Conda环境并安装CPU版本
echo 4. 创建Conda环境并安装GPU版本

choice /c 123 /n

if %errorlevel% equ 1 (
    pip install -r requirement.txt
    echo 完成
) else if %errorlevel% equ 2 (
    conda install cudatoolkit -y
    pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
    pip install -r requirement.txt
        echo 完成
) else if %errorlevel% equ 3 (
    conda create -n fast-phasr-next python==3.12
    conda activate fast-phasr-next
    pip install -r requirement.txt
    echo 完成，请使用conda activate fast-phasr-next激活环境～
) else if %errorlevel% equ 4 (
    conda create -n fast-phasr-next python==3.12
    conda activate fast-phasr-next
    conda install cudatoolkit -y
    pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
    pip install -r requirement.txt
        echo 完成，请使用conda activate fast-phasr-next激活环境～
) else (
    echo 无效的选择
)