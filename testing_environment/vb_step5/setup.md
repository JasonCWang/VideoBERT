# Documentation for Step 5 of VideoBERT Process

## Initial Setup

I believe it might be due to the fact that we are running these python scripts from shell scripts, but there have been many occassions where running the `train.py` file results in an error saying it cannot find the VideoBERT package, so it is unable to import functions like 'evaluate()' or or VideoBERT objects.

As a result, I have found that manually appending the module to the system path is a successful workaround for this issue.  At the very top of the `train.py` file, I have added the following code:

    import sys
    sys.path.append('/home/mike/VideoBERT')
    
    sys.stdout = open('/home/mike/videobert_step5/logs/stdout_output1.txt', 'w')

The first two lines are what manually appends the VideoBERT package to the system path at the start of the file, so the rest of the imports work correctly.

The second half of the coded segment just redirects all of the stdout into a textfile.  This was very helpful in recording all of the loss values as they were generated.

<br>

## Running the Training Script

In order to run the `train.py` python file, perform the following steps:

1. Within this directory, set up the following:
    * logs directory (if one doesn't already exist)
    * output directory (these will be contain all checkpoints produced during this training instance).  You can make different output directories to easily create different training instances.

2. Within `train.py` edit the first few lines at the top of the header to correctly point to the right filepath of VideoBERT, and also to redirect the stdout to the appropriate place (if desired)

3. In the logging settings of `train.py`, edit the output of the log files to go to the desired location.  (For example, in the code below, the logs will go to an output1.log file contained in the log directory)

This is on ~ line 465 in `train.py`:

    logging.basicConfig(
        format="%(asctime)s - %(levelname)s - %(name)s -   %(message)s",
        datefmt="%m/%d/%Y %H:%M:%S",
        level=logging.INFO if args.local_rank in [-1, 0] else logging.WARN,
        filename=args.log_dir + '/output1.log'
    )

<br> 

4. As we found during our research, the GPU encountered shape issues while training, so we initially started training everything on the CPU.  In order to train on the CPU, just set device accordingly

This is ~ line 460 in `train.py`:

    For CPU only, assign devices as follows:

        device = torch.device("cpu")

    Otherwise, set device accordingly, which will use GPU if it is detected, and otherwise use the CPU.

        device = torch.device('cuda:{}'.format(torch.cuda.  current_device()) if torch.cuda.is_available() else "cpu")

5. Then set the appropriate arguments within the `run_training.sh` script in this directory.  There are a lot of optional arguments, and you can refer to which one corresponds to what effect in the readme in the main directory.  Note that you will need to reference the training and evaluation files that you created in Step 4.

6. Run the `run_training.sh` script.

<br>

Once you start the training process, checkpoints will be written intermittently to the output directory as declared in the shell script arguments.

Here are a few key settings that I used to make training a bit more manageable:

**--save_steps**: 
>"Save checkpoint every X updates steps".

Saving a checkpoint takes quite a bit of time, so setting this to a higher value (i.e. 5000 or 10000) will allow you to make more progress before having to spend a lot of time saving a checkpoint.

**--save_total_limit**:  
>"Limit the total amount of checkpoints, delete the older checkpoints in the output_dir, does not delete by default".  

Highly recommend using this setting.  If this is not set, you can easily run out of hard drive space on your system, since each checkpoint is approximately 3.5gb.  Set this value to a low number such as 3 or 5 to ensure each training instance does not take up that much space.

**--model_name_or_path**:
> "The model checkpoint for weights initialization. Leave None if you want to train a model from scratch."

This field is used in tandem with --should_continue in order to continue training from a specific checkpoint.  This is useful if you need to stop the training for whatever reason (such as switching from CPU based training to GPU based training).

**--should_continue**:
> "Whether to continue from latest checkpoint in output_dir"

This must be set in addition to the --model_name_or_path flag in order for the training to actually pick up from a checkpoint.