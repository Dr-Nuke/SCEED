# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 18:33:57 2019

@author: ChrisBo
"""

# ok lets pretend we could apply the neuronal networ to thisdata set

from __future__ import absolute_import, division, print_function, unicode_literals

import pandas as pd 
import csv

# TensorFlow and tf.keras
import tensorflow as tf
from tensorflow import keras

# Helper libraries
import numpy as np
import matplotlib.pyplot as plt


data=pd.read_csv('large.csv')
data=data.iloc[0:10,:] # reduce for the moment
solution=pd.read_csv('jeopardy.csv')

m=data.size # size of trainig set
perm=np.random.permutation(m)

