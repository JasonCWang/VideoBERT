# Documentation for Step 3 of VideoBERT Process

## Minibatch HKMeans
In order to run the hkmeans script, you need to already have the I3D video features extracted to some place on the system.

Then, you will need to update the arguments in the `run_hkmeans.sh` script contained within this folder.  You can refer to the markdown file in the main directory to see where the appropriate arguments should go.  There are already 'centroids' and 'vectors' directories contained within this folder to use, but they still need to be updated in the shell script.

Once this step is run, the _centroids_ directory should be filled with many numpy centroid files, and the _vectors_ directory should be empty.  Once this is confirmed, you can proceed to the next step.

**Note**: If at any point you want to restart this step from the beginning (i.e. if you encounter runtime issues), you can run the `reset.sh` script.  This will simply destroy and recreate new instances of the centroids/ and vectors/ directories.

***

## Centroid to Image:
The centroid to image script is necessary because the centroids that we generated in HKMeans do not have images associated with them.  In order to perform downstream tasks such as video forecasting (which uses centroids as future video token predictions), we need to have an image associated with each centroid.

    Note: Before starting the concatenating centroids portion, one approach for handling the mismatched shapes of the centroids compared to raw datapoints was to take the column-wise mean of the centroids in order to make a (1, 600) shape centroid.  This would have been done here.  You also need to make sure that when the `centroid_to_img.py` script reads in the concatenated averaged centroids, that it reads in one at a time, and not 20 at a time.

### Concatenating the centroids
Prior to mapping the centroid to an image, the system requires that all of the centroids generated in the previous HKmeans step be concatenated into a single Numpy file.  In order to create the concatenated centroid, I created a `concatenate_centroids.py` file that exists in `VideoBERT/VideoBERT/data/concatenate_centroids.py`.  This can be used by following these steps:

1. Within this directory, create a _concatenated_centroids.npy_ file.  Leave this empty.

2. Within the `concatenated_centroids.py` script, update the `CENTROID_DIR` and the `CONCATENATED_CENTROID` to reflect the centroid directory and the concatenated numpy file that was created in step 1, respectively.

3. Run `concatenated_centroids.py`

**Note**: I used numpy.vstack() in order to concatenate these numpy functions instead of numpy.concatenate().  This is best explained with an example.

    Suppose we have two centroids of shape (20, 600).  When we concatenate the files, we want the centroids to be aligned one after the other, not combined.  Numpy.concatenate() yields a result with the shape (20, 1200).  However, in order to be properly ingested by centroid_to_img.py, we want to have the shape (40, 600).  In order to accomplish this, we need to use Numpy's vstack() function instead.
    
After the centroids have been concatenated, you are ready to run the `centroid_to_img.py` script by following the next set of instructions:

1. Create a `centroid_to_img.json` file within this directory to be used to contain the mapping of centroids to images.

2. Update the arguments within the `run_cti.sh` script in this directory.  Reference for what values should be used for which argument can be found on the main VideoBERT directory.

3. Run the `run_cti.sh` shell script.

Performing the previous steps should populate the `centroid_to_img.json` file created earlier with mappings to image files generated from the I3D video break-down process.