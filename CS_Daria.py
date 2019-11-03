#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 11:13:16 2019

@author: Daria
"""
import csv

import numpy

import matplotlib.pyplot as plt

import math as m


### Caushy distribution with parameters
def Caushy (x, g, x0, A):
    return float((A/m.pi)*g/((x-x0)**2+g*g))


cif = '\ufeffcif'
cif = 'cif'


#data_all_X = []
#data_all_Y = []
#data_susp_X = []
#data_susp_Y = []


a1_all_X = []
a1_all_Y = []
a1_susp_X = []
a1_susp_Y = []
a1_non_X = []
a1_non_Y = []




with open('large.csv', 'r') as data:
    reader = csv.DictReader(data, delimiter = ",")     
    for line in reader:
        if int(line['category']) == 0 and int(line['age']) > 0 and int(line['age']) >0:
           
            
            a1_all_X.append(float(line['io_ratio']))
            a1_all_Y.append(float(line['transaction_count']))
            if int(line[cif]) in susplist:
                a1_susp_X.append(float(line['io_ratio']))
                a1_susp_Y.append(float(line['transaction_count']))
            else:
                a1_non_X.append(float(line['io_ratio']))
                a1_non_Y.append(float(line['transaction_count']))
            
        

#### OBSERVE how different the distributions are!!!!
        
plt.plot(a1_not_X, a1_not_Y, 'bs')
plt.plot (a1_susp_X, a1_susp_Y, 'k^')
plt.show()        



### HERE the choice of parameters was performed
### the tails of both distributions are too heavy to be gaussian
### so the Caushy distribution was chosen
### now the parameters are chosen manually, that can easily be improved 
### (optimisation problem solved by gradient descent technique ex.g)



gn = 0.07
x0n = 0.3
An = 200

gs = 0.045
x0s = 0.41
As = 250

x = np.arange(0., 1., 0.01)
ys = [Caushy(xx, gs, x0s, As) for xx in x]
yn = [Caushy(xx, gn, x0n, An) for xx in x]

#### the curves describes nicely the shape of the data
plt.plot(a1_non_X, a1_non_Y, 'bs')
plt.plot (a1_susp_X, a1_susp_Y, 'ks')
plt.plot(x, yn, 'g-')
plt.plot(x, ys, 'r-')
plt.plot(flag_x, flag_y, 'r^')
plt.show()

### final parameters for not suspicious people
pn = (gn,x0n,An)



def outlayers_D (io, trans, param, eps = 50):
### this function detect people acting suspicious comparing the following parameters:
### IO_ratio and transaction number
### not suspicious people fit perfectly inside the bell of Caushy distribution
### suspicious people lie in the distribution with different parameters
### returns True if the person doesn't fit the first bell
    
### the parameters for the Caushy distribution could be found more sophisticatly

### the parameret eps is an error margin, can be determined nices
### but even taken to be 0 gives only 6(!) not suspicious people out of the line
    F0 = Caushy(io, param[0], param[1], param[2])
    if F0 + eps < trans:
        return True
    else:
        return False




### that gonna be the list of rised flags
FLAG_D = []

flag_x = []
flag_y = []


with open('large.csv', 'r') as data:
    
    reader = csv.DictReader(data, delimiter = ",")     
    for line in reader:
        if int(line['category']) == 0 and int(line['age']) > 0:
           if outlayers_D(float(line['io_ratio']), float(line['transaction_count']), pn):
               flag_x.append(float(line['io_ratio']))
               flag_y.append(float(line['transaction_count']))
               FLAG_D.append(int(line[cif]))


plt.plot(a1_non_X, a1_non_Y, 'bs')
plt.plot (a1_susp_X, a1_susp_Y, 'ks')
plt.plot(x, yn, 'g-')
plt.plot(flag_x, flag_y, 'r^')
plt.show() 



#### THERE SOME DATA PLAYS WERE PERFORMED
# =============================================================================

#data_1 = []
#data_num = []
#data_susp = []
#dd_turnover = []
#dd_counterp = []
#dd_chrisk = []
#
#dd_toNtrans = []
#





def normalize(v):
    norm = np.linalg.norm(v)
    if norm == 0: 
       return v
    return v / norm

# =============================================================================
# 
# data_0 = []
# #with open('large.csv', 'r') as small:
# with open('small.csv', 'r') as small:
# # 
#     reader = csv.DictReader(small, delimiter = ",")
#     for line in reader:
#         if float(line['atm_withdrawal'])+float(line['atm_deposit']) == 0:
#             CASH_IO_ratio = 0
#         else:
#             CASH_IO_ratio = float(line['atm_deposit'])/(float(line['atm_withdrawal'])+float(line['atm_deposit']))
#     
# #        dd = [float(line['io_ratio']), CASH_IO_ratio, int(line['is_pep']),float(line['turnover']), int(int(line['n_of_accounts'])>3)]
#         
#         age = []
#         
#         
#         
#         dd = [float(line['io_ratio']), 
#               CASH_IO_ratio, 
#               int(line['is_pep']),
#               (line['turnover']), 
#               int(line['distinct_counterparties']),
#               1.0, 
#               0*int(int(line['n_of_accounts'])>3),
#               0.0
#               ]
#         
#         cif = '\ufeffcif'#'cif'#
#         dd_turnover.append(float(line['turnover']))
#         dd_counterp.append(int(line['distinct_counterparties']))
#         dd_chrisk.append(float(line['channel_risk']))
#         
#         dd_toNtrans.append(m.exp(float(line['turnover'])/float(line['transaction_count'])))
#         
#         data_num.append(int(line[cif]))
#         data_susp.append(int(line[cif]) in susplist)
#         data_1.append(dd)
#         
# #
# 
# l = len(data_1)
# 
# dd_norm_turnover = normalize(dd_turnover)
# dd_norm_chrisk = normalize(dd_chrisk)
# 
# dd_norm_toNtrans = normalize(dd_toNtrans)
# 
# 
# #ss_dd_counterp = int(sum(dd_counterp)/l)
# 
# for i in range(l):
#     data_1[i][3] = 0*dd_norm_turnover[i]
#     data_1[i][4] = 0*int(data_1[i][4] > 10 * ss_dd_counterp)
#     data_1[i][5] = 0*dd_norm_chrisk[i]
#     data_1[i][7] = dd_norm_toNtrans[i]
# 
# 
# for i in range(l):
#     dd_0 = [dd_norm_toNtrans[i]]
#             #data_1[i][0],
#             #data_1[i][1]]
#     data_0.append(dd_0)
# 
# from sklearn.cluster import KMeans
# 
# numb_clust =20
# 
# clf= KMeans(init='k-means++', random_state=241, n_clusters = numb_clust)
# clf.fit(data_0)
#     
# X = clf.predict(data_0)
# 
# RES = []
# for n in range(numb_clust):
#     stot = sum([X[i] == n for i in range(len(X))])
#     susptot = sum([X[i] == n and data_susp[i] == 1 for i in range(len(X))])
#     RES.append([susptot/stot, stot])
# 
# print(sum([RES[i][0]>0 for i in range(numb_clust)]))
# =============================================================================
# =============================================================================
# 
# 
# with open('small.csv', 'r') as small:
# #with open('large.csv', 'r') as small:
# 
#     reader = csv.DictReader(small, delimiter = ",")
# 
#










































    
#    NUM_cash = 0
#    reader = csv.DictReader(small, delimiter = ",")
#    
#    
#    N_hyst = 40
#    CASH_percent = [0,]*N_hyst
#    hyst_CASH_percent = []
#    
#    
#    INDIVID = 0
#    ACTIVE = 0
#    SAVING = 0
#    
#    
#    
#    
#    NOT_USE_CASH = 0
#    SUSP_NOT_USE_CASH = 0
#    #we're interested in only individual clients
#    
#    
#    
#    PUT_CASH = 0
#    
#    young = 0
##    young_susp = 0
##    young_susp_1 = 0
##    YS = 0
##    YS_1 = 0
##    
#    
#    ys = 0
#    ys_0 = 0
#    
#    
#    
#    
#    for line in reader:
##        NUM_cash = 0
#        
#        is_pers = (int(line['category']) == 0)
#        INDIVID += is_pers
#        
#        trans_income = (1-float(line['io_ratio']))*float(line['turnover'])
#        trans_outcome = (float(line['io_ratio']))*float(line['turnover'])
#        
#        tot_income = trans_income + float(line['atm_deposit'])
#        tot_outcome = trans_outcome + float(line['atm_withdrawal'])
#        
#        ###drawing hystogram for cash use percentage
#        
#        TOT_USED = trans_outcome+float(line['atm_withdrawal'])
#        
#        if TOT_USED == 0:
#            perc_cash = 0
#        else:
#            perc_cash = float(line['atm_withdrawal'])/TOT_USED
#        
#        #hyst_CASH_percent.append(perc_cash)
#        
#        
#        not_use_cash = (perc_cash<CASH_bound)*is_pers
#        
#        NOT_USE_CASH += not_use_cash
#        
#        active = (float(line['inactive_days_average'])<inact_DAYS_1)*(float(line['inactive_days_max'])<inact_DAYS_2)
#        #if active == 0:
#            #print(float(line['inactive_days_average']), float(line['inactive_days_max']))
#            
#        ACTIVE += active*(int(line['category']) == 0)
#        
#        is_saving = (float(line['io_ratio']) > SAVING_bound)
#        SAVING += is_saving*is_pers
#        
#        SUSP_NOT_USE_CASH += not_use_cash*(1-active)*is_saving
#        
#        
#        
#        
#        tot_put = 0
#        
#        
#        
#        
#        #HERE NOTHING WORKS - no correspondence between suspicious and not
##        if line['age'] != None:
##            if int(line['age']) < AGE and int(line['age']) > 0:
##                IO = float(line['io_ratio'])
##                
##                if tot_income+tot_outcome == 0:
##                    IO_ad = 0
##                else:
##                    IO_ad = tot_income/(tot_income+tot_outcome)
##                
##                young += 1
##                #2*abs(IO - 0.5)*float(line['turnover'])
##                if abs(IO-0.5)<IO_DELTA and float(line['turnover']) > MUCH_MONEY:
##                    young_susp += 1
##                    if int(line['cif']) in susplist:
##                        YS += 1
##                    
##                if abs(IO_ad-0.5)<IO_DELTA and float(line['turnover']) > MUCH_MONEY:
##                    young_susp_1 += 1
##                    if int(line['cif']) in susplist:
##                        YS_1 += 1
#        
#        
#        if line['age'] != None:
#            if int(line['age']) < AGE and int(line['age']) > 0:
#
#                if  float(line['atm_withdrawal'])> 100000:
#                    ys += 1
#                    #if int(line['\ufeffcif']) in susplist:
#                    if int(line['cif']) in susplist:
#                        ys_0 += 1                    
#
#
#print(INDIVID, NOT_USE_CASH, SUSP_NOT_USE_CASH)
#print(ACTIVE, SAVING)
#
#
#print(ys, ys_0)
##print(young, young_susp, YS, young_susp_1, YS_1)
#
#
#
#
##plt.hist(hyst_CASH_percent, bins = N_hyst)



###AS IT IS ALREADY ONCE READ - NEAD TO BE UNCOMMENTED
#susplist = []
#with open('jeopardy.csv', 'r') as susp:
#    
#    reader = csv.DictReader(susp, delimiter = ",")
#    
#    for line in reader:
#        if int(line['suspicious']) == 1:
#            susplist.append(int(line[cif]))
#            #print('y')
#    
#
#print(len(susplist))        
#    
    
#parameters that we set here^ but then up to correct
#CASH_bound = 0.005
#
#inact_DAYS_1 = 150
#inact_DAYS_2 = 16
#
#SAVING_bound = 0.9
#
#AGE = 21
#
#IO_DELTA = 0.005
#MUCH_MONEY = 10000000
#
####RED FLAGS ABOUT 
#cc = 0
#
#
#YOUNG =0
#YOUNG_TURNOVER =0

#with open('large.csv', 'r') as small:
#    reader = csv.DictReader(small, delimiter = ",")
#    
#    for line in reader:
#        cc+= 1
#        if int(line['age']) >0 :
#            if int(line['age']) < AGE:
#                YOUNG += 1
#                YOUNG_TURNOVER += float(line['turnover'])
#                
#                
#print(YOUNG_TURNOVER/YOUNG)                





#data_large = pandas.read_csv("large.csv")
#data_small = pandas.read_csv("small.csv")
#
#data_ind_small = data_small[data_small['category'] == 0]
#
#
#
#
#
#
#