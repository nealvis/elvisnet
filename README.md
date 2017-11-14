# elvisnet
neural network for identifying era of elvis images

# readme for elvisnet scripts

## training
* Clone the repo
* cd into the scripts diretory
* if you are using CPU to train modify the solver.prototxt file so that solver_mode is CPU 
* python3 create_train_test.py
* ./convert_lmdb.sh
* ./create_mean.sh
* ./download_model.sh
* ./train.sh

## running on NCS
* make sure deploy.prototxt, elvisnet_mean.binaryproto, and caffe_googlenet_train.caffemodel are in the directory 
* python3 convert_protomean.py elvisnet_mean.binaryproto elvisnet_mean.npy
* make compile to create the graph file 
* python3 run.py

look at this link for guidance.  https://chunml.github.io/ChunML.github.io/project/Training-Your-Own-Data-On-Caffe/
