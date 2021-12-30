# This file will be for concatenating the centroids as part of step 3 of the VideoBERT Repository

import os
import glob
import numpy as np
import pdb

# Since we only need to do this once for now, I will hard-code the paths.  In the future, it would be
# good to parse arguments from the terminal for paths
dir_of_centroids = '/home/mike/step3_centroids/'
os.chdir('/home/mike/step3_centroids')

with open('/home/mike/concatenated_centroid_01.npy', 'wb') as f_handle:
    all_arrays = []
    for npfile in glob.glob(dir_of_centroids + '*.npy'):
        all_arrays.append(np.load(os.path.join(dir_of_centroids, npfile)))
    all_arrays = np.array(all_arrays)
    # pdb.set_trace()
    np.save(f_handle, all_arrays)
