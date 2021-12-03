from tensorflow.python.client import device_lib
import tensorflow as tf
import sys
import os

def get_available_gpus():
    local_device_protos = device_lib.list_local_devices()
    return [x.name for x in local_device_protos if x.device_type == 'GPU']

def select_gpu_from_available():
    available_gpus = get_available_gpus()

    print("Available GPUs: ", available_gpus)
    gpu_index = input(f"Which GPU (index) would you like to use: ")
    device_name = f'/device:GPU:{gpu_index}'
    print(f"You have selected {device_name} to use for this computation")
    return device_name

if __name__ == '__main__':
    # Set debugging so we can see what GPUs are being leveraged
    tf.debugging.set_log_device_placement(True)

    device_name = select_gpu_from_available()

    # Phony tensorflow operations with designated GPU
    with tf.device(device_name):
        a = tf.constant([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
        b = tf.constant([[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]])
        c = tf.matmul(a, b)
    
    # With the matmul OUTSIDE of the with statement, tf will default back to the default GPU:0
    # c = tf.matmul(a, b)
    