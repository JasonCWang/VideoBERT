# Documentation for Step 4 of VideoBERT Process

## Obtaining the captions for HowTo100M Dataset

The captions for the HowTo100M dataset have already been generated for us, which eliminates any need for the Automatic Speech Recognition component of recreating VideoBERT.  Instead, we just need to download it from their website [here](https://www.rocq.inria.fr/cluster-willow/amiech/howto100m/).

However, captions json file is not stored in this repository itself because it is a few GB large.  Therefore, you need to download it yourself wherever you would like to use it.

In order to download the captions directly to this directory, you can run the command:

    wget https://www.rocq.inria.fr/cluster-willow/amiech/howto100m/howto100m_captions.json

This will create the file `howto100m_captions.json` file in the directory in which you ran the command.

***

## Labelling Data

The labelling data portion of the VideoBERT process essentially labels the raw data with video tokens by using the centroids that were generated in Step 3 of the VideoBERT process.  

In order to run the `label_data.py` script within VideoBERT, complete the following steps:

1. Create a `labelled_data.json` file in the current directory.  This is where all of the labelled data will be stored.

1. Replace the arguments in the `run_label.sh` shell script with the appropriate fields.  You can find a template for which arguments go where in the main directory.  Keep in mind that the concatenated centroids argument will be obtained from Step 3 of the VideoBERT process.

2. Run the `run_label.sh` shell script command

This will create a `labelled_data.json` file that is a dictionary with video IDs and corresponding centroid tokens for each video ID.  From assessing the `label_data.py` script, it labels data by performing HKmeans with the existing centroids, and then attributing raw data to each of the existing centroids.

***

## Punctuate Text

Since the captions are provided to us with the HowTo100M dataset, they are not correctly bound to the video.  In other words, we still need to match the captions up with the corresponding video components.

Before doing this, however, we also need to punctuate the text, since the provided captions have no punctuation.

For the punctuation task, I requested access to the PCL model from PyPi's punctuator module, which has been stored in the repository so you do not have to request access each time.

In our initial attempts at training, I used the **Demo-Europarl-EN.pcl** punctuator file.  Other punctuator models can be used to see if it impacts results.

<br>

In order to run the `punctuate_text.py` script, perform the following steps:

1. Replace the arguments in the `run_punctuate.sh` script with the appropriate values.

2. Run `run_punctuate.sh`

**Note**: There is NO need to create an empty `full_training_data.json` file in the current directory.  The way the `punctuate_text.py` script works is by determining whether the file exists, and creating a new one if it does not.  If an the file exists before running the script, it will read the file and pick up where it left off.  Therefore, if there is an empty file at the time the script starts, it will crash because it cannot read the empty file as a json object.

Once this step is performed, it will generate the `full_training_data.json` file or other training data file with the name specified in the shell script arguments.

***

## Creating the Evaluation Set

By default, the initial documented process does not create an evaluation set from the data it has been handling.  Since we know that we will want an evaluation set for future testing, I have created an elementary script that creates an evaluation set from the training set that was just generated.

The `create_evaluation_set.py` script lives in:

    /VideoBERT/VideoBERT/data/create_evaluation_set.py

And it essentially siphons off a portion of the training data and places it into a new json file.

In order to run this script, perform the following directions:

1. Create 2 new files - one file for the new training data without the evaluation data, and another file for the evaluation data.

2. Navigate to `create_evaluation_set.py` by following the above file path.

3. Edit TRAINING_FILE_PATH, TRAINING_WO_EVAL, EVALUATION_FILE_PATH to point to the training file, the training file without evaluation data, and the evaluation file, respectively

4. Edit the EVALUATION_PROPORTION to change how large the evaluation dataset will be.  (For example, 0.2 would create an 80/20 split between training and evaluation data, respectively)

5. Run `create_evaluation_set.py`

Performing these steps will create an evaluation set and a new training set.



