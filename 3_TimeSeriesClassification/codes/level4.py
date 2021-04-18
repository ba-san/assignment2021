import os, math
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def dtw_self_implemented_v2(ref, test):
    # Initialization

    Cumul = [[float('inf') for i in range(256+1)] for j in range(256+1)]
    Cumul[0][0] = 0.0

   # Main loop
    for i in range(1,1+256):
        for j in range(1,1+256):
            dist = 0
            for k in range(64):
                dist += abs(ref[k]-test[k
            #dist = abs(x1[i-1]-x2[j-1])**2+abs(y1[i-1]-y2[j-1])**2+abs(z1[i-1]-z2[j-1])**2 # euclidean distance for this
            Cumul[i][j] = dist + min(Cumul[i-1][j], Cumul[i][j-1], Cumul[i-1][j-1])

    return math.sqrt(Cumul[len(x1)][len(x2)])

def level3(path):
    with open( '../dataset/level4/reference/1/data1.dat') as v1:
        v1_data = v1.readlines()
        
    with open( '../dataset/level4/reference/1/data2.dat') as v2:
        v2_data = v2.readlines()

    with open(path) as f:
        s = f.readlines()
        
        # get data
        ref1 = [0 for i in range(64)]
        ref2 = [0 for i in range(64)]
        test = [0 for i in range(64)]
        
        for i in range(64):
            ref1[i] = [float(v1_data[j].split('\t')[i]) for j in range(len(v1_data))]
            ref2[i] = [float(v2_data[j].split('\t')[i]) for j in range(len(v2_data))]
            test[i] = [float(s[j].split('\t')[i]) for j in range(len(s))]
        
        # calc dtw
        distance1 = dtw_self_implemented_v4(ref1, test)
        distance2 = dtw_self_implemented_v4(ref2, test)
        
        print('self implemented dtw| class1:{} class2:{}\n'.format(distance1, distance2))
        
if __name__=="__main__":    
    for i in range(14):
        path = '../dataset/level4/test/data{}.dat'.format(i+1)
        level3(path)
