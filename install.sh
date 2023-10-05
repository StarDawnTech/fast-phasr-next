#!/bin/bash

echo "Fast-Phasr-Next————新一代轻量级Diffsinger自动音素标注工具"
echo "十分推荐您创建一个Conda环境！Conda环境就像冰箱里的盒子一样保证不串味！"
options=("1. 安装CPU版本" "2. 安装GPU版本" "3. 创建Conda环境")

echo "请选择一个选项："
select choice in "${options[@]}"; do
    case $REPLY in
        1)
            pip install -r requirement.txt
            echo "完成"
            break
            ;;
        2)
            conda install cudatoolkit -y
            pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
            pip install -r requirement.txt
            echo "完成"
            break
            ;;
        3)
            conda create -n fast-phasr-next python==3.12
            echo "请使用conda activate fast-phasr-next激活环境～并安装环境"
            break
            ;;
        *)
            echo "无效的选择"
            ;;
    esac
done