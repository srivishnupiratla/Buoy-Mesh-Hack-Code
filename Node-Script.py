#This is the script for all the normal nodes in this mesh network. These nodes have to send and recive so they have both functions built into them.

import RFM69
from RFM69registers import *
import datetime
import time
import base64
import tensorflow as tf
import sys
import os
import shutil
from os import listdir
from os import mkdir
from shutil import copyfile
from os.path import isfile, join
import time
import numpy as np
import cv2
import time
import serial
import keyboard
from flask import Flask
from flask import render_template
import customfunctions

cap = cv2.VideoCapture(0)
x=0

def mainpicclass:
    label_lines = [line.rstrip() for line in tf.gfile.GFile("hotglue/retrainedlabels.txt")]

    with tf.gfile.FastGFile("hotglue/retrainedgraph.pb", 'rb') as f:
        graph_def = tf.GraphDef()
        graph_def.ParseFromString(f.read())
        _ = tf.import_graph_def(graph_def, name='')
    while True:
        cap = cv2.VideoCapture(1)
        ret,frame = cap.read()
        cv2.imwrite('c1.png',frame)

        cap.releaase()

        with tf.Session() as sess:
            softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')

        image_data =  tf.gfile.FastGFile('c1.png', 'rb').read()

        predictions = sess.run(softmax_tensor, \
                    {'DecodeJpeg/contents:0': image_data})

        top_k = predictions[0].argsort()[-len(predictions[0]):][::-1]
        firstElt = top_k[0];

        newFileName = label_lines[firstElt] +"--"+ str(predictions[0][firstElt])[2:7]+".jpg"

        if (label_lines[firstElt] == "cod fish"):
            print ("cod(S) found, Alert Triggered")



        for node_id in top_k:
            human_string = label_lines[node_id]
            score = predictions[0][node_id].val()

            for valcus in node_id in top_k:
                return valcus().nums()



def sendfeed:

        rm = RFM69.RFM69(RF69_915MHZ, 1, 1, True)
        print "class initialized"
        print "reading all registers"
        results = rm.readAllRegs()
        for result in results:
            print result
        print "Performing rcCalibration"
        rm.rcCalibration()
        print "setting high power"
        rm.setHighPower(True)
        print "Checking temperature"
        print "picture.take"
        print "setting encryption"
        rm.encrypt("1234567891011121")
        print "sending blah to 2"
        if rm.sendWithRetry(2, "," (mainpiclass().join(cat /sys/bus/w1/devices/10-000802b4ba0e/w1_slave).join([chr(letter) for letter in test.DATA]), test.SENDERID, test.RSSI), 3, 20):
            print "ack recieved"
        print "reading"
        while True:
            rm.receiveBegin()
            while not test.receiveDone():
                time.sleep(.1)
            print "%s from %s RSSI:%s" % ("".join([chr(letter) for letter in test.DATA]), test.SENDERID, test.RSSI)
            if rm.ACKRequested():
                rm.sendACK()



while true:
    sendfeed()
    time.sleep(10000)
