# elvisnet
neural network for identifying era of elvis images

# readme for elvisnet scripts

* Clone the repo
* cd into the scripts diretory
* if you are using CPU to train modify the solver.prototxt file so that solver_mode is CPU 
* python3 create_train_test.py
* ./convert_lmdb.sh
* ./create_mean.sh
* ./download_model.sh
* ./train.sh

look at this link for guidance.  https://chunml.github.io/ChunML.github.io/project/Training-Your-Own-Data-On-Caffe/
