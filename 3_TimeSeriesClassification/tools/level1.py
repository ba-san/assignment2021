#https://qiita.com/hcpmiyuki/items/251586526c5924f09aa3

import os
import numpy as np
import matplotlib.pyplot as plt
from fastdtw import fastdtw

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
        plt.title(os.path.basename(path)+"    1:{:.5g}  2:{:.5g}".format(distance1, distance2))
        #plt.show()
        fig.savefig(path+".png")

if __name__=="__main__":
    

    for i in range(6):
        path = '../dataset/level1/test/{}.dat'.format(i+1)
        level1(path)
