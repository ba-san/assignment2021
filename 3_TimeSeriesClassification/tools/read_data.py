
import os
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def read_file1(path):
    with open(path) as f:
        s = f.readlines()
        #for i in range(len(s)):
            #print(s[i])

        
        x = list(range(len(s)))
        y = [float(s[i]) for i in range(len(s))]

        fig = plt.figure()
        plt.plot(x, y)
        plt.ylim(-1,1)
        plt.title(os.path.basename(path), fontsize=18)
        #plt.show()
        fig.savefig(path+".png")

def read_file2(path):
    with open(path) as f:
        s = f.readlines()
        
        n = list(range(len(s)))
        x = [float(s[i].split('\t')[0]) for i in range(len(s))]
        y = [float(s[i].split('\t')[1]) for i in range(len(s))]
        z = [float(s[i].split('\t')[2]) for i in range(len(s))]
        
        #print(x)
        #print(y)
        #print(z)
        #exit()
        
        fig = plt.figure()
        ax = Axes3D(fig)
        ax.plot(x, y, z)
        plt.title(os.path.basename(path))
        plt.show()
        fig.savefig(path+".png")
        
if __name__=="__main__":
    path='/home/daisuke/Documents/assignment2021/3_TimeSeriesClassification/dataset/level2/reference/2.dat'
    read_file2(path)
