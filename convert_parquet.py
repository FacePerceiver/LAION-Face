import torch
import pyarrow.parquet as pq
import pyarrow as pa
import os
from tqdm import tqdm
import argparse

if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("sample_list")
    parser.add_argument("laion_meta_dir")
    parser.add_argument("laion_face_meta_dir")
    args=parser.parse_args()
    all_count=0
    laion_meta_dir=args.laion_meta_dir
    all_samples=torch.load(args.sample_list)
    os.makedirs(args.laion_face_meta_dir,exist_ok=True)

    for split_num in tqdm(range(32)):
        samples=set(all_samples[split_num])
        sn=str(split_num).zfill(5)
        big_parquet_file=f"{laion_meta_dir}/part-{sn}-5b54c5d5-bbcf-484d-a2ce-0d6f73df1a36-c000.snappy.parquet"
        big_table=pq.read_table(big_parquet_file).to_pandas()
        big_table["has_face"]=big_table["SAMPLE_ID"].map(lambda x:x in samples)
        big_table=big_table[big_table["has_face"]]
        del big_table["has_face"]
        all_count+=len(big_table)
        pq.write_table(pa.Table.from_pandas(big_table), os.path.join(args.laion_face_meta_dir,f'laion_face_part_{sn}.parquet'))
