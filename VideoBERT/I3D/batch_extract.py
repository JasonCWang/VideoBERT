import sys
sys.path.append('/home/mkc5372/VideoBERT/')
from VideoBERT.I3D.extract_features import extract_features
from gpu_inform import select_gpu_from_available
import tensorflow as tf
import os.path
import argparse
import pathlib


parser = argparse.ArgumentParser()

parser.add_argument('-f', '--file-list-path', type=str, required=True, help='path to file containing video file names')
parser.add_argument('-r', '--root-video-path', type=str, required=True, help='root directory containing video files')
parser.add_argument('-s', '--features-save-path', type=str, required=True, help='directory in which to save features')
parser.add_argument('-i', '--imgs-save-path', type=str, required=True, help='directory in which to save images')
args = parser.parse_args()

'''
    Need to set the appropriate GPU name here that we want to use for the batch_extract process

    For GPUs, these names take the form:
    
        '/device:GPU:##'

    Where ## is a 0-based index number from the GPU's available.
'''

# Uncomment debugging line below to see what GPUs are being used
tf.debugging.set_log_device_placement(True)
device_name = select_gpu_from_available()
print("device name:", device_name)

video_file_list_path = args.file_list_path
video_root_path = args.root_video_path
features_save_path = args.features_save_path
imgs_save_path = args.imgs_save_path

pathlib.Path(features_save_path).mkdir(parents=True, exist_ok=True)
pathlib.Path(imgs_save_path).mkdir(parents=True, exist_ok=True)

with open(video_file_list_path, 'r') as fd:
    # video_files = list(map(lambda l: l.strip()[31:], fd.readlines()))
    video_files = []
    for video_name in fd.readlines():
        video_files.append(video_name.strip() + '.mp4')

video_paths = [os.path.join(video_root_path, f) for f in video_files]

print(len(video_paths), 'video paths found.')

from_index = 0

for i, path in enumerate(video_paths[from_index:]):

    try:
        print('processing:', path, '[{}/{}]'.format(i+1, len(video_paths[from_index:])))

        folder_name = os.path.splitext(os.path.basename(path))[0]
        specific_feature_save_path = os.path.join(features_save_path, folder_name)
        specific_img_save_path = os.path.join(imgs_save_path, folder_name)

        if os.path.exists(specific_feature_save_path):
            print(specific_feature_save_path, "Already exists, moving on to next folder")
            continue

        pathlib.Path(specific_feature_save_path).mkdir(parents=True, exist_ok=True)
        pathlib.Path(specific_img_save_path).mkdir(parents=True, exist_ok=True)

        # i3d.features_save_dir = save_path
        extract_features(device_name, path, specific_feature_save_path, specific_img_save_path)

        print('completion status:', path, '[SUCCESS]')
    except Exception as e:
        print(e)
        print('completion status:', path, '[FAILED]')
