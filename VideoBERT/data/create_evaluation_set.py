# Creates an evaluation json file for the training process

import json
import os
import pdb

TRAINING_FILE_PATH = '/home/mike/videobert_step4/training_data.json'
TRAINING_WO_EVAL = '/home/mike/videobert_step4/training_data_wo_eval.json'
EVALUATION_FILE_PATH = '/home/mike/videobert_step4/evaluation_data.json'
EVALUATION_PROPORTION = 0.2

if __name__ == '__main__':
    # Read in the current training file
    training_data = json.load(open(TRAINING_FILE_PATH, 'r'))
    training_data_size = len(training_data)
    training_keys = list(training_data.keys())

    if os.path.exists(EVALUATION_FILE_PATH):
        os.remove(EVALUATION_FILE_PATH)

    if os.path.exists(TRAINING_WO_EVAL):
        os.remove(TRAINING_WO_EVAL)

    with open(EVALUATION_FILE_PATH, 'w') as f_handle, open(TRAINING_WO_EVAL, 'w') as w_handle:
        training_after_eval = training_data
        counter = 0
        eval = {}
        while (counter < training_data_size * EVALUATION_PROPORTION):
            eval[training_keys[counter]] = training_data[training_keys[counter]]
            training_after_eval.pop(training_keys[counter])
            counter += 1
        # pdb.set_trace()
        json.dump(eval, f_handle)
        json.dump(training_after_eval, w_handle)