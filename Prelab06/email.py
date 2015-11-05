#! /usr/bin/env python3.4
import re
__author__ = 'ee364e03'

if __name__ == '__main__':
    pattern2="purdue.edu"
    with open('Part2.in','r') as myFile:
         all_lines=myFile.readlines()
         for line in all_lines:
             m2=re.sub(pattern2,"ecn.purdue.edu",line)
             m2 = m2[:-2]
             m2=m2+"/100"
             print(m2)






