#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 28 12:20:45 2018

@author: Dharun Ramakrishnan
"""

import glob
import cv2
import time
import os
#import paracept as pc

def process(filename, key):
    image = filename
#    image = cv2.imread(filename)
#    key +=1
    print(image.shape)
    r = 100.0 / image.shape[1]
    dim = (100, int(image.shape[0] *r))
    imageresized = cv2.resize(image,(300,300),dim,interpolation = cv2.INTER_AREA)    
    cv2.imwrite( 'imageresized_{}.jpg'.format(key) ,imageresized )
    print('imageresized_{}.jpg'.format(key))
    os.remove('images/yo{}.JPG'.format(key))

while True:
    for (i,image_file) in enumerate(glob.iglob('images/*.jpg')):
        time.sleep(1)
        print(os.path.isfile(image_file))
        img = cv2.imread(image_file)
        i += 1
        cv2.imwrite('images/yo{}.JPG'.format(i), img)
        os.remove(image_file)
        process(img, i)
#        pc.accept_and_die(img)

