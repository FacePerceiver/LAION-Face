#! /bin/bash
folder="$1"
mkdir $folder
for i in $(seq 0 31)
do
    echo "start download face detection $i"
    while true 
    do
    if [ -s $folder/sample2detect_$i.pth ]; then
            break
    else
      wget --no-proxy https://huggingface.co/datasets/FacePerceiver/laion-face/resolve/main/sample2detect_$i.pth -O $folder/sample2detect_$i.pth
    fi
    done
    echo "end download part $i"
done
