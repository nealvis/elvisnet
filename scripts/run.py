#! /usr/bin/env python3

# Copyright(c) 2017 Intel Corporation. 
# License: MIT See LICENSE file in root directory.


from mvnc import mvncapi as mvnc
import sys
import numpy
import cv2
import time
import csv
import os
import sys

dim=(224,224)
EXAMPLES_BASE_DIR='../../'

# ***************************************************************
# get labels
# ***************************************************************
labels=["50s", "60s", "70s"]

# ***************************************************************
# configure the NCS
# ***************************************************************
mvnc.SetGlobalOption(mvnc.GlobalOption.LOG_LEVEL, 2)

# ***************************************************************
# Get a list of ALL the sticks that are plugged in
# ***************************************************************
devices = mvnc.EnumerateDevices()
if len(devices) == 0:
	print('No devices found')
	quit()

# ***************************************************************
# Pick the first stick to run the network
# ***************************************************************
device = mvnc.Device(devices[0])

# ***************************************************************
# Open the NCS
# ***************************************************************
device.OpenDevice()

network_blob='graph'

#Load blob
with open(network_blob, mode='rb') as f:
	blob = f.read()

graph = device.AllocateGraph(blob)

# ***************************************************************
# Load the image
# ***************************************************************
ilsvrc_mean = numpy.load(EXAMPLES_BASE_DIR+'caffe/ElvisNet/elvisnet_mean.npy').mean(1).mean(1) #loading the mean file
img = cv2.imread(EXAMPLES_BASE_DIR+'caffe/ElvisNet/50s/17.jpg')
img=cv2.resize(img,dim)
img = img.astype(numpy.float32)
img[:,:,0] = (img[:,:,0] - ilsvrc_mean[0])
img[:,:,1] = (img[:,:,1] - ilsvrc_mean[1])
img[:,:,2] = (img[:,:,2] - ilsvrc_mean[2])

# ***************************************************************
# Send the image to the NCS
# ***************************************************************
graph.LoadTensor(img.astype(numpy.float16), 'user object')

# ***************************************************************
# Get the result from the NCS
# ***************************************************************
output, userobj = graph.GetResult()

# ***************************************************************
# Print the results of the inference form the NCS
# ***************************************************************
order = output.argsort()[::-1][:6]
print('\n------- predictions --------')
for i in range(0,3):
	print ('prediction ' + str(i) + ' (probability ' + str(output[order[i]]) + ') is ' + labels[order[i]] + '  label index is: ' + str(order[i]) )


# ***************************************************************
# Clean up the graph and the device
# ***************************************************************
graph.DeallocateGraph()
device.CloseDevice()
    



