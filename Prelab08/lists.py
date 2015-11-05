#! /usr/bin/env python3.4
import copy
from sys import *
import os

__author__ = 'ee364e03'

def find_median(fst,snd):
    A=fst+snd
    A.sort()
    length=len(A)
    if length%2 ==0:
        ind=int(length/2-1)
    else:
        ind=int((length+1)/2)
    B=(A[ind],A)
    return B


if __name__ == '__main__':
    fst = input('Enter the first list of numbers: ')
    snd = input('Enter the second list of numbers:')
    fst=fst.split()
    ind=0
    for item in fst:
        i=int(item)
        fst[ind]=i
        ind+=1
    snd=snd.split()
    ind=0
    for item in snd:
        i=int(item)
        snd[ind]=i
        ind+=1
    print('First list:{}'.format(fst))
    print('Second list:{}'.format(snd))
    user_out=find_median(fst,snd)
    print('Merged list:{}'.format(user_out[1]))
    print('Median:{}'.format(user_out[0]))

