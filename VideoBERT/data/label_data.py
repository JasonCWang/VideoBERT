import numpy as np
from tqdm import tqdm
from sklearn.cluster import MiniBatchKMeans
import os
import json

features_root = 'saved_features'
dirs = os.listdir(features_root)

centroids = np.load('centroids.npy')
kmeans = MiniBatchKMeans()
kmeans.cluster_centers_ = centroids

save_path = 'labelled_data.json'

data_dict = {}

for folder in tqdm(dirs):
    data_dict[folder] = []
    feature_files = sorted(os.listdir(os.path.join(features_root, folder)))
    for features in feature_files:
        data_dict[folder].extend(kmeans.predict(np.load(os.path.join(features_root, folder, features))))
    data_dict[folder] = list(map(lambda x: int(x), data_dict[folder]))

json.dump(data_dict, open(save_path, 'w'), sort_keys=True, indent=4)