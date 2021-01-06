import os
import numpy as np
import pandas as pd
from collections import Counter


dataset_root = '/nfs/masi/CXR_public/PADCHEST_gdrive'

label_file = os.path.join(dataset_root, 'label/PADCHEST_chest_x_ray_images_labels_160K_01.02.19.csv')
image_dir = os.path.join(dataset_root, 'image')


def run_padchest_analysis():
    analysis_label_file()


def analysis_label_file():
    label_df = pd.read_csv(label_file, dtype = str)

    print('Projection (ALL)')
    print(Counter(label_df['Projection'].to_list()))

    print('Projection determine method')
    print(Counter(label_df['MethodProjection'].to_list()))

    # print('PhotometricInterpretation')
    # print(Counter(label_df['PhotometricInterpretation_DICOM'].to_list()))

    print('------------*------------')
    print(f'Demography information below is for those with VP information manually reviewed')
    print('------------*------------')

    print('Projection (Manual review of DICOM fields)')
    vp_manual_review_df = label_df[label_df['MethodProjection'] == 'Manual review of DICOM fields']
    print(Counter(vp_manual_review_df['Projection'].to_list()))

    print('Number of scans')
    print(vp_manual_review_df.shape[0])

    print('Number of subjects')
    full_list = vp_manual_review_df['PatientID'].to_list()
    subject_list = list(set(full_list))
    print(len(subject_list))

    print('Gender')
    print(Counter(vp_manual_review_df['PatientSex_DICOM'].to_list()))

    print('Pediatric')
    print(Counter(vp_manual_review_df['Pediatric'].to_list()))

    print('PhotometricInterpretation')
    print(Counter(vp_manual_review_df['PhotometricInterpretation_DICOM'].to_list()))

    # print('Age stratification')
    #




