import numpy as np
import pandas as pd
import os
from collections import Counter
from datasets.utils import read_file_contents_list


dataset_root = '/nfs/masi/CXR_public/CXR8'
image_dir = os.path.join(dataset_root, 'images/images')
label_csv = os.path.join(dataset_root, 'Data_Entry_2017_v2020.csv')
train_val_list = os.path.join(dataset_root, 'images/train_val_list.txt')


def run_nih_cxr_analysis():
    get_vp_demography()


def get_vp_demography():
    label_df = pd.read_csv(label_csv)

    vp_all = label_df['View Position'].to_list()
    print('VP counter for all:')
    print(Counter(vp_all))

    # Get the train_val subset
    train_val_file_name_list = read_file_contents_list(train_val_list)
    label_dict = label_df.set_index('Image Index').to_dict('index')

    vp_train_val = []
    for file_name in train_val_file_name_list:
        vp_flag = label_dict[file_name]['View Position']
        vp_train_val.append(vp_flag)

    print('VP counter train/val')
    print(Counter(vp_train_val))
