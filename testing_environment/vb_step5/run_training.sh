#!/bin/bash

python /home/mike/VideoBERT/VideoBERT/train/train.py --output_dir /home/mike/vb_step5/gpu_out1 --train_data_path /home/mike/vb_step4/short_training_data.json --eval_data_path /home/mike/vb_step4/evaluation_data.json --per_gpu_train_batch_size 8 --learning_rate 1e-5 --num_train_epochs 8 --logging_steps 1000 --save_steps 5000 --log_dir /home/mike/vb_step5/logs --save_total_limit 5