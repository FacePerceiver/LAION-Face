folder="$1"
mkdir $folder
for i in $(seq 0 31)
do
    echo "start download face detection $i"
    wget https://huggingface.co/datasets/FacePerceiver/laion-face/resolve/main/sample2detect_$i.pth -O $folder/sample2detect_$i.pth
    echo "end download part $i"
done