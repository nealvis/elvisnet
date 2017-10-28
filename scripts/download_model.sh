#!/bin/bash

#PROTOTXT_FILENAME= deploy.prototxt
#GET_PROTOTXT = wget -P . https://raw.githubusercontent.com/BVLC/caffe/master/models/bvlc_googlenet/deploy.prototxt

#CAFFEMODEL_FILENAME = bvlc_googlenet.caffemodel
#GET_CAFFEMODEL = wget -P . -N http://dl.caffe.berkeleyvision.org/${CAFFEMODEL_FILENAME}

#wget -P . http://raw.githubusercontent.com/BVLC/caffe/master/models/bvlc_googlenet/solver.prototxt
#sed -i 's/models\/bvlc_googlenet\/train_val.prototxt/elvisnet_googlenet\/train_val.prototxt/' solver.prototxt
#sed -i 's/models\/bvlc_googlenet\/bvlc_googlenet/elvisnet_googlenet\/caffe_googlenet_train/' solver.prototxt

#wget -P . http://raw.githubusercontent.com/BVLC/caffe/master/models/bvlc_googlenet/train_val.prototxt
#sed -i 's/^.*mean_value:.*$//g' ./train_val.prototxt
#sed -i 's/transform_param {/transform_param {\n    mean_file: "elvisnet_mean.binaryproto"/g' ./train_val.prototxt


mkdir elvisnet_googlenet
mv solver.prototxt elvisnet_googlenet/
mv train_val.prototxt elvisnet_googlenet/

