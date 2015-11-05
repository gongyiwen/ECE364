#! /usr/bin/env python3.4
import copy
from sys import *
import os
__author__ = 'ee364e03'

if __name__ == '__main__':
    filename=argv[1]
    try:
        fp = open(filename,"r") #possible exception
    except:
        print('{} is not a readable file'.format(filename))
        exit(1)
    #all_lines=myFile.read()
    #lines=all_lines.split('\n')
    for line in fp:
            line=line.split()
            length=0
            sum=0
            word_list=[]
            for item in line:
                try:
                    i=float(item)
                    sum+=i
                    length+=1
                except ValueError:
                    word_list.append(item)
            word_list=' '.join(word_list)
            if length > 0:
                avg=sum/length
                avg=format(avg,'.3f')
                print('{0} {1}'.format(avg,word_list))
            else:
                print('{}'.format(word_list))
    fp.close()
    exit(0)



