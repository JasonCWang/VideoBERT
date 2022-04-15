# Script used for crudely plotting loss data generated from training the model

import matplotlib.pyplot as plt
from pdb import set_trace

if __name__ == '__main__':
    
    loss = [] 
    text_loss = []
    video_loss = []
    joint_loss = []
    line_counter = 0
    num_benchmarks_taken = 0
    num_benchmarks_to_read = 90     # 40 benchmark reports into the stdout_output2_2.txt is about where epoch 1 ends

    with open('/home/mike/videobert_step5/logs/stdout_output2_2.txt') as f:
        lines = f.readlines()

        for line in lines:
            # Total Loss line
            if line_counter == 1:
                words = line.split()
                loss.append(float(words[1]))
                line_counter += 1

            # Text loss line
            elif line_counter == 2:
                words = line.split()
                text_loss.append(float(words[1]))
                line_counter += 1

            # Video loss line
            elif line_counter == 3:
                words = line.split()
                video_loss.append(float(words[1]))
                line_counter += 1

            # Joint loss line
            elif line_counter == 4:
                words = line.split()
                joint_loss.append(float(words[1]))
                line_counter = 0

            # Initial hook
            if (line == 'Benchmark Eval:\n'):
                line_counter = 1
                num_benchmarks_taken += 1
                if num_benchmarks_taken == num_benchmarks_to_read:
                    break

    loss_yaxis = [loss[i] for i in range(0, len(loss))]
    loss_xaxis = [i for i in range(0, len(loss))]

    plt.figure(1)
    plt.plot(loss_xaxis, loss_yaxis)
    plt.title('Loss vs Iteration')
    plt.xlabel('Iteration (times ~500)')
    plt.ylabel('Loss')
    plt.savefig('/home/mike/videobert_step5/benchmark_total_loss3.png')
    plt.clf()

    text_yaxis = [text_loss[i] for i in range(0, len(text_loss))]
    text_xaxis = [i for i in range(0, len(text_loss))]

    plt.plot(text_xaxis, text_yaxis)
    plt.title("Text Loss vs Iteration")
    plt.xlabel("Iteration (times ~500)")
    plt.ylabel("Text Loss")
    plt.savefig('/home/mike/videobert_step5/benchmark_text_loss3.png')
    plt.clf()

    video_yaxis = [video_loss[i] for i in range(0, len(video_loss))]
    video_xaxis = [i for i in range(0, len(video_loss))]

    plt.plot(video_xaxis, video_yaxis)
    plt.title("Video Loss vs Iteration")
    plt.xlabel("Iteration (times ~500)")
    plt.ylabel("Video Loss")
    plt.savefig('/home/mike/videobert_step5/benchmark_videoloss_graph3.png')
    plt.clf()

    joint_yaxis = [joint_loss[i] for i in range(0, len(joint_loss))]
    joint_xaxis = [i for i in range(0, len(joint_loss))]

    plt.plot(joint_xaxis, joint_yaxis)
    plt.title("Joint Loss vs Iteration")
    plt.xlabel("Iteration (times ~500)")
    plt.ylabel("Joint Loss")
    plt.savefig('/home/mike/videobert_step5/benchmark_jointloss_graph3.png')
    plt.clf()

    # #######################

    # loss_yaxis = [loss[i] for i in range(0, len(loss), 5)]
    # loss_xaxis = [i for i in range(0, len(loss), 5)]

    # plt.figure(1)
    # plt.plot(loss_xaxis, loss_yaxis)
    # plt.title('Total Loss vs Iteration')
    # plt.xlabel('Iteration')
    # plt.ylabel('Loss')
    
    # text_yaxis = [text_loss[i] for i in range(0, len(text_loss), 5)]
    # text_xaxis = [i for i in range(0, len(text_loss), 5)]

    # plt.plot(text_xaxis, text_yaxis)

    # video_yaxis = [video_loss[i] for i in range(0, len(video_loss), 5)]
    # video_xaxis = [i for i in range(0, len(video_loss), 5)]

    # plt.plot(video_xaxis, video_yaxis)

    # joint_yaxis = [joint_loss[i] for i in range(0, len(joint_loss), 5)]
    # joint_xaxis = [i for i in range(0, len(joint_loss), 5)]

    # plt.plot(joint_xaxis, joint_yaxis)
    # plt.savefig('/home/mike/videobert_step5/allloss_graph.png')
