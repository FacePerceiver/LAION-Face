## LAION-Face

LAION-Face is the human face subset of [LAION-400M](https://laion.ai/laion-400-open-dataset/), it consists of 50 million image-text pairs. Face detection is conducted to find images with faces. Apart from the 50 million full-set(LAION-Face 50M), we also provide a 20 million sub-set(LAION-Face 20M) for fast evaluation. 

LAION-Face is first used as the training set of [FaRL](https://github.com/FacePerceiver/FaRL), which is a powerful pre-training transformer backbones for face analysis tasks.

*For now, we only provide the image id list of those contains human face, you need download the images by yourself following the following instructions. We will further provide the face detection metadata.*

## Setup
```
pip install -r requirements.txt
```
We need `pyarrow` to read and write parque file, `img2dataset` to download images.

### Download the metadata

We provide the list of sample_id in [huggingface](https://huggingface.co/datasets/FacePerceiver/laion-face/resolve/main/laion_face_ids.pth).

Download and convert the metadata with the following commands. 

```bash
wget -l1 -r --no-parent https://the-eye.eu/public/AI/cah/laion400m-met-release/laion400m-meta/
mv the-eye.eu/public/AI/cah/laion400m-met-release/laion400m-meta/ .
wget https://huggingface.co/datasets/FacePerceiver/laion-face/resolve/main/laion_face_ids.pth
python convert_parquet.py ./laion_face_ids.pth ./laion400m-meta ./laion_face_meta
```

### Download the images with img2dataset
When metadata is ready, you can start download the images.

```bash
bash download.sh ./laion_face_meta ./laion_face_data
```

Please be patient, this command might run over days, and cost about 2T disk space, and it will download 50 million image-text pairs as 32 parts.

- To use the **LAION-Face 50M**, you should use all the 32 parts.
- To use the **LAION-Face 20M**, you should use use these parts.
    ```
    0,2,5,8,13,15,17,18,21,22,24,25,28
    ```

checkout `download.sh` and [img2dataset](https://github.com/rom1504/img2dataset) for more details and parameter setting.



### License
LAION-Face is the face subset of [LAION-400M](https://laion.ai/blog/laion-400-open-dataset), we distribute the image id list (the pth files) under the most open Creative Common CC-BY 4.0 license, which poses no particular restriction. The metadata of the dataset are from [LAION-400M](https://laion.ai/blog/laion-400-open-dataset). Please check [LAION-400M](https://laion.ai/blog/laion-400-open-dataset) for more details.


### Contact 
For help or issues concerning the data, feel free to submit a GitHub issue, or contact [Yinglin Zheng](mailto:zhengyinglin@stu.xmu.edu.cn).

## Citation

If you find our work helpful, please consider citing 
```
@article{zheng2021farl,
  title={General Facial Representation Learning in a Visual-Linguistic Manner},
  author={Zheng, Yinglin and Yang, Hao and Zhang, Ting and Bao, Jianmin and Chen, Dongdong and Huang, Yangyu and Yuan, Lu and Chen, Dong and Zeng, Ming and Wen, Fang},
  journal={arXiv preprint arXiv:2112.03109},
  year={2021}
}
```