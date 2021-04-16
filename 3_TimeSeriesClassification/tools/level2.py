#https://qiita.com/hcpmiyuki/items/251586526c5924f09aa3

import os, math
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from fastdtw import fastdtw

def dtw_self_implemented_v2(x1, y1, z1, x2, y2, z2):
    # Initialization
    Cumul = [[float('inf') for i in range(len(x1)+1)] for j in range(len(x2)+1)]
    Cumul[0][0] = 0.0

   # Main loop
    for i in range(1,1+len(x1)):
        for j in range(1,1+len(x2)):
            dist = abs(x1[i-1]-x2[j-1])**2+abs(y1[i-1]-y2[j-1])**2+abs(z1[i-1]-z2[j-1])**2 # euclidean distance for this
            Cumul[i][j] = dist + min(Cumul[i-1][j], Cumul[i][j-1], Cumul[i-1][j-1])

    return math.sqrt(Cumul[len(x1)][len(x2)])


def level2_v2(path):
    with open( '../dataset/level2/reference/1.dat') as v1:
        v1_data = v1.readlines()
        
    with open( '../dataset/level2/reference/2.dat') as v2:
        v2_data = v2.readlines()

    with open(path) as f:
        s = f.readlines()
        
        # get data
        x_v1 = [float(v1_data[i].split('\t')[0]) for i in range(len(v1_data))]
        y_v1 = [float(v1_data[i].split('\t')[1]) for i in range(len(v1_data))]
        z_v1 = [float(v1_data[i].split('\t')[2]) for i in range(len(v1_data))]

        x_v2 = [float(v2_data[i].split('\t')[0]) for i in range(len(v2_data))]
        y_v2 = [float(v2_data[i].split('\t')[1]) for i in range(len(v2_data))]
        z_v2 = [float(v2_data[i].split('\t')[2]) for i in range(len(v2_data))]
        
        x = [float(s[i].split('\t')[0]) for i in range(len(s))]
        y = [float(s[i].split('\t')[1]) for i in range(len(s))]
        z = [float(s[i].split('\t')[2]) for i in range(len(s))]
        
        # calc dtw (smalle is better)
        distance1 = dtw_self_implemented_v2(x_v1, y_v1, z_v1, x, y, z)
        distance2 = dtw_self_implemented_v2(x_v2, y_v2, z_v2, x, y, z)
        
        print('self implemented dtw| class1:{} class2:{}\n'.format(distance1, distance2))
        
        # prep graph
        fig = plt.figure()
        title = "{}    1:{:.5g}  2:{:.5g}".format(os.path.basename(path), distance1, distance2)
        ax = Axes3D(fig, auto_add_to_figure=False)
        fig.add_axes(ax)
        ax.plot(x, y, z)
        ax.plot(x_v1, y_v1, z_v1)
        ax.plot(x_v2, y_v2, z_v2)
        ax.text2D(0.1,0.9,title, transform=ax.transAxes, fontsize=18)
        #plt.show()
        fig.savefig(path+".png")
        
if __name__=="__main__":    
    for i in range(6):
        path = '../dataset/level2/test/{}.dat'.format(i+1)
        level2(path)
