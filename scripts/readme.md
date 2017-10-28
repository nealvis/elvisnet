# readme for elvisnet scripts

* python3 create_train_test.py
    * creates the test_index.txt and test_index.txt files
    
* ./convert_lmdb.sh
    * creates the lmdb for test and training data
    * in elvisnet_test_lmdb and elvisnet_train_lmdb directories
    
* ./create_mean.sh
    * Creates the elvisnet_mean.binaryproto file with mean values for training data

* ./download_model.sh
    * creates elvisnet_googlenet directory
    * Copies the solver.prototxt and train_val.prototxt into the new directory

* ./train.sh
    * Trains the model with the images



