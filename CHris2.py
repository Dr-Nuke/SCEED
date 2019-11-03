# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 17:40:58 2019

@author: ChrisBo
"""

import numpy as np
import csv
import math

## row count
#with open('jeopardy.csv') as csv_file:


#with open('jpardy.eocsv', newline='') as csvfile:    
#    reader = csv.DictReader(csvfile)
#    for row in reader:
#        print(row['cif'],row['suspicious'])
#with open('jeopardy.csv', newline='') as f:
#    
##    data=np.zeros([row_count-1,3],dtype=int32)
#    csv_reader = csv.reader(f)
#    csv_headings = next(csv_reader)
#    for row in csv_reader:
#        print(np.array([int(row[0]),int(row[1])]))
#  

from numpy import genfromtxt
data = genfromtxt('jeopardy.csv', delimiter=',')
#remove header
data=np.delete(data, (0), axis=0);


su=np.array([90000029,
90000087,
90000126,
90000155,
90000206,
90000246,
90000259,
90000308,
90000335,
90000340,
90000362,
90000409,
90000477,
90000635,
90000647,
90000675,
90000719,
90000759,
90000774,
90000780,
90000857,
90000884,
90000942,
90000952,
90000964,
90000998])

for i in su:
   print(data[data[:,0]==i,:])
   
   