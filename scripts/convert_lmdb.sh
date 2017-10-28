#!/bin/bash

GLOG_logtostderr=1 convert_imageset --resize_height=256 --resize_width=256 --shuffle ./ ./train_index.txt ./elvisnet_train_lmdb

GLOG_logtostderr=1 convert_imageset --resize_height=256 --resize_width=256 --shuffle ./ ./test_index.txt ./elvisnet_test_lmdb


