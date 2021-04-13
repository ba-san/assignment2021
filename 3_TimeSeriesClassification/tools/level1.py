#https://qiita.com/hcpmiyuki/items/251586526c5924f09aa3

import os
import math
import numpy as np
import matplotlib.pyplot as plt
from tslearn.metrics import dtw

def dtw_self_implemented(x, y):
    # Initialization
    Cumul = [[float('inf') for i in range(len(x)+1)] for j in range(len(y)+1)]
    Cumul[0][0] = 0.0

   # Main loop
    for i in range(1,1+len(x)):
        for j in range(1,1+len(y)):
            dist = abs(x[i-1]-y[j-1])**2 # euclidean distance for this
            Cumul[i][j] = dist + min(Cumul[i-1][j], Cumul[i][j-1], Cumul[i-1][j-1])

    return math.sqrt(Cumul[len(x)][len(y)])

def level1(path):
    with open( '../dataset/level1/reference/1.dat') as v1:
        v1_data = v1.readlines()
        
    with open( '../dataset/level1/reference/2.dat') as v2:
        v2_data = v2.readlines()

    with open(path) as f:
        s = f.readlines()
        
        # get data
        x = list(range(len(s)))
        v1_dlist = [float(v1_data[i]) for i in range(len(v1_data))]
        v2_dlist = [float(v2_data[i]) for i in range(len(v2_data))]
        y = [float(s[i]) for i in range(len(s))]
        
        # calc dtw (smalle is better)
        distance1, path1 = fastdtw(v1_dlist, y)
        distance2, path2 = fastdtw(v2_dlist, y)
        
        # prep graph
        fig = plt.figure()
        plt.plot(x, y)
        plt.plot(x, v1_dlist)
        plt.plot(x, v2_dlist)
        plt.ylim(-1,1)
        plt.title(os.path.basename(path)+"    1:{:.5g}  2:{:.5g}".format(distance1, distance2), fontsize=18)
        #plt.show()
        fig.savefig(path+".png")
        
def level1_v2(path):
    with open( '../dataset/level1/reference/1.dat') as v1:
        v1_data = v1.readlines()
        
    with open( '../dataset/level1/reference/2.dat') as v2:
        v2_data = v2.readlines()

    with open(path) as f:
        s = f.readlines()
        
        # get data
        x = list(range(len(s)))
        v1_dlist = [float(v1_data[i]) for i in range(len(v1_data))]
        v2_dlist = [float(v2_data[i]) for i in range(len(v2_data))]
        y = [float(s[i]) for i in range(len(s))]
        
        # calc dtw (smalle is better)
        #distance1, path1 = fastdtw(v1_dlist, y)
        #distance2, path2 = fastdtw(v2_dlist, y)
        
        # dtw(k-means) tslearn
        #dba_km = TimeSeriesKMeans(n_clusters=3,
        #                             n_init=2,
        #                             metric="dtw")
        
        distance1 = dtw(v1_dlist, y)
        distance2 = dtw(v2_dlist, y)
        
        distance1_me = dtw_self_implemented(v1_dlist, y)
        distance2_me = dtw_self_implemented(v2_dlist, y)
        print(distance1, distance1_me, distance2, distance2_me)
        exit()
        
        # prep graph
        fig = plt.figure()
        plt.plot(x, y)
        plt.plot(x, v1_dlist)
        plt.plot(x, v2_dlist)
        plt.ylim(-1,1)
        plt.title(os.path.basename(path)+"    1:{:.5g}  2:{:.5g}".format(distance1, distance2), fontsize=18)
        #plt.show()
        fig.savefig(path+"v2.png")

if __name__=="__main__":
    

    for i in range(6):
        path = '../dataset/level1/test/{}.dat'.format(i+1)
        level1_v2(path)
