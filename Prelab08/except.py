#! /usr/bin/env python3.4
import copy
from sys import *
import os
__author__ = 'ee364e03'

if __name__ == '__main__':
    A=input('Please enter some values:')
    A=A.split()
    sum=0
    for item in A:
        try:
            i=float(item)
            sum+=i
        except ValueError:
            continue
    print('The sum is: {}'.format(sum))