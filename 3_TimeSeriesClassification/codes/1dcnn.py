import torch
import torch.nn as nn
import os, math
import numpy as np

class Net1D(nn.Module):
    def __init__(self):
        super(Net1D, self).__init__()
        self.conv1 = nn.Conv1d(1, 8, kernel_size=3, stride=1)
        self.bn1 = nn.BatchNorm1d(8)
        self.relu = nn.ReLU()
        self.maxpool = nn.MaxPool1d(kernel_size=3, stride=2)
        
        self.conv2 = nn.Conv1d(8, 16,kernel_size=3, stride=1)
        self.bn2 = nn.BatchNorm1d(16)
        self.conv3 = nn.Conv1d(16,64,kernel_size=3, stride=1)
        self.gap = nn.AdaptiveAvgPool1d(1)
        self.fc = nn.Linear(64,2)
    
    def forward(self,x):
        x = self.conv1(x)
        x = self.bn1(x)
        x = self.relu(x)
        x = self.maxpool(x)

        x = self.conv2(x)
        x = self.bn2(x)
        x = self.relu(x)
        x = self.maxpool(x)

        x = self.conv3(x)
        x = self.gap(x)
        x = x.view(x.size(0),-1)
        x = self.fc(x)
        return x


        
if __name__=="__main__":    
    model = Net1D()
    in_data = torch.randn(8, 1, 50)
    print(in_data)
    out_data = model(in_data)
    print(out_data)
    print(out_data.size())
