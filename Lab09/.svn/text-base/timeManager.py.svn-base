#! /usr/bin/env python3.4
import copy
from sys import *
import os
import re
from timeDuration import *

__author__ = 'ee364e03'
def getTotalDuration(experimentName):
    with open('Experiments.txt','r')as myFile:
        all_lines=myFile.readlines()
        all_lines=all_lines[3:]
        A={}
        for line in all_lines:
            line.strip()
            linelist=line.split()
            min=int(linelist[1].split(':')[0])
            #print(min)
            sec=int(linelist[1].split(':')[1])
            #print(sec)
            other=int(linelist[2])
            #print(other)
            B=Duration(0,min,sec)
            if other > 0:
                C=B.__mul__(other)
            else:
                C=Duration(0,0,0)
            if linelist[0] not in A:
                A[linelist[0]]=C
            else:
                A[linelist[0]]=A[linelist[0]].__add__(C)
        return A[experimentName]





def rankExperiments(*args):
    B=[]
    C=[]
    for i in args:
        B.append((getTotalDuration(i).getTotalSeconds(),i))
    B.sort()
    print(B)
    length=len(B)
    for item in range(length):
        _,x=B[item]
        C.append(x)
    C.reverse()
    return C




if __name__ == '__main__':
    pass
