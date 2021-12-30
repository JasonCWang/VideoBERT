# This file will be for concatenating the centroids as part of step 3 of the VideoBERT Repository
#
#   Author: Michael Chan (mkc5372)
#   Date:   Dec 2021

import os
import glob
import numpy as np
import pdb


CENTROID_DIR = '/home/mike/videobert_step3/step3_average_centroids'
CONCATENATED_CENTROID = '/home/mike/videobert_step3/concatenated_centroid.npy'


if __name__ == '__main__':
    # Every time we run this script, delete the existing concatenated file
    if os.path.exists(CONCATENATED_CENTROID):
        os.remove(CONCATENATED_CENTROID)

    # Now, create the file and append all average centroids to it
    with open(CONCATENATED_CENTROID, 'wb') as f_handle:
        for root, dir, filenames in os.walk(CENTROID_DIR):
            all_arrays = np.concatenate([np.load(CENTROID_DIR + os.path.sep + file) for file in filenames])
            np.save(f_handle, all_arrays)
