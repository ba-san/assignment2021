
import os
import numpy as np
import matplotlib.pyplot as plt


def read_file(path):
    with open(path) as f:
        s = f.readlines()
        #for i in range(len(s)):
            #print(s[i])

        
        x = list(range(len(s)))
        y = [float(s[i]) for i in range(len(s))]

        fig = plt.figure()
        plt.plot(x, y)
        plt.ylim(-1,1)
        plt.title(os.path.basename(path))
        #plt.show()
        fig.savefig(path+".png")

if __name__=="__main__":
    

	for i in range(1):
		path = '../dataset/level2/test/{}.dat'.format(i+1)
		read_file(path)
		path = '../dataset/level3/test/{}.dat'.format(i+1)
		read_file(path)
		path = '../dataset/level4/test/{}.dat'.format(i+1)
		read_file(path)
