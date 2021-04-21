import os, math
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def dtw_self_implemented_v4(ref, test):
    # Initialization
    Cumul = [[float('inf') for i in range(256+1)] for j in range(256+1)]
    Cumul[0][0] = 0.0

   # Main loop
    for i in range(1,1+256):
        for j in range(1,1+256):
            dist = 0
            for k in range(64): # 64-dimension euclidean distance
                dist += abs(ref[k][i-1]-test[k][j-1])**2
            Cumul[i][j] = dist + min(Cumul[i-1][j], Cumul[i][j-1], Cumul[i-1][j-1])

    return math.sqrt(Cumul[256][256])

def level4(path):
    distance1_sum, distance2_sum = 0, 0
    distance_dict = {}
    for t in range(3):
        with open( '../dataset/level4/reference/1/data{}.dat'.format(t+1)) as v1:
            v1_data1 = v1.readlines()
            
        with open( '../dataset/level4/reference/2/data{}.dat'.format(t+1)) as v2:
            v2_data1 = v2.readlines()
    
        with open(path) as f:
            s = f.readlines()
            
            # get data
            ref1 = [[0]*256 for i in range(64)]
            ref2 = [[0]*256 for i in range(64)]
            test = [[0]*256 for i in range(64)]
            
            for i in range(64):
                ref1[i] = [float(v1_data1[j].split('\t')[i]) for j in range(len(v1_data1))]
                ref2[i] = [float(v2_data1[j].split('\t')[i]) for j in range(len(v2_data1))]
                test[i] = [float(s[j].split('\t')[i]) for j in range(len(s))]
            
            # calc dtw
            distance1 = dtw_self_implemented_v4(ref1, test)
            distance2 = dtw_self_implemented_v4(ref2, test)
            distance_dict["class1_{}".format(t+1)] = distance1
            distance_dict["class2_{}".format(t+1)] = distance2
            
            distance1_sum += distance1
            distance2_sum += distance2

    # kNN
    sorted_dict = sorted(distance_dict.items(), key=lambda x:x[1])
    print(sorted_dict)
    cnt = 0
    class1_cnt = 0
    for t in sorted_dict:
        if(cnt==3):
            break
        if("class1" in t[0]):
            class1_cnt+=1
        cnt+=1
    
    # result
    print('*' * 80)
    print('average dtw| class1:{} class2:{}'.format(distance1_sum/3.0, distance2_sum/3.0))
    print('*' * 80)
    print("kNN (k=3)| class1:{} class2:{}".format(class1_cnt, 3-class1_cnt))
    print('*' * 80)
    print('\n')
        
if __name__=="__main__":
    distance1_list = [[0]*3 for i in range(14)]
    distance2_list = [[0]*3 for i in range(14)]
    
    for i in range(14):
        path = '../dataset/level4/test/data{}.dat'.format(i+1)
        level4(path)
