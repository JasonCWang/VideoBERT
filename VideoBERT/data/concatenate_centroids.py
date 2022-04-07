# This file will be for concatenating the centroids as part of step 3 of the VideoBERT Repository
# The numpy files are concatenated such that they can still be read-in in individual centroid
# values.  For example, concatenating two (1, 600) average centroids should yield (2, 600) instead
# of (1, 1200).  This is because in the centroid_to_img.py script, it iterates through individual centroids, just
# all from one single numpy file.
#
#   Author: Michael Chan (mkc5372)
#   Date:   Dec 2021

import os
import glob
import numpy as np
import pdb


# CENTROID_DIR = '/home/mike/videobert_step3/step3_average_centroids'
# CONCATENATED_CENTROID = '/home/mike/videobert_step3/concatenated_centroid.npy'

# A second attempt at the entire process contained within 'vb_step#' folders
CENTROID_DIR = '/home/mike/vb_step3/centroids'
CONCATENATED_CENTROID = '/home/mike/vb_step3/concatenated_centroid.npy'


if __name__ == '__main__':
    # Every time we run this script, delete the existing concatenated file
    if os.path.exists(CONCATENATED_CENTROID):
        os.remove(CONCATENATED_CENTROID)

    # Now, create the file and append all average centroids to it
    with open(CONCATENATED_CENTROID, 'wb') as f_handle:
        for root, dir, filenames in os.walk(CENTROID_DIR):
            # This operation should be fine because our Average Centroids should all be (1, 600) shape
            # np.vstack will create the concatenated centroid of shape (2, 600) wrt the example at the top of the file
            all_arrays = np.vstack([np.load(CENTROID_DIR + os.path.sep + file) for file in filenames])

            # np.concatenate yields the (1, 1200) shape that we don't want, but it is commented here for documentation
            # all_arrays = np.concatenate([np.load(CENTROID_DIR + os.path.sep + file) for file in filenames])
            np.save(f_handle, all_arrays)
