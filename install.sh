#!/bin/bash

echo "Fast-Phasr-Next————新一代轻量级Diffsinger自动音素标注工具"
options=("1. 安装CPU版本" "2. 安装GPU版本")

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
        *)
            echo "无效的选择"
            ;;
    esac
done