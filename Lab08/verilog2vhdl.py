#! /usr/bin/env python3.4
import copy
from sys import *
import os
import re
from vtools import *

def convertLine(verilogLine):
    try:
        m=parseNetLine(verilogLine)
    except ValueError:
        str='Error: Bad Line.'
        return str
    pattern=r"\s*(\w+)\s+(\w+)\s*(\(){1}([\.\s*\w+\(\w+\)\,]+)\)"
    vhdlline=m[1]+':'+' '+m[0]+' '+'PORT '+'MAP('
    for item in m[2]:
        port=item[0]
        pin=item[1]
        line=port+'=>'+pin
        vhdlline+=line+', '
    vhdlline=vhdlline[:-2]+');'
    print(vhdlline)
    return vhdlline


def convertFile(sourceFile,targetFile):
    fp=open(sourceFile,'r')
    fp1=open(targetFile,'w')
    for line in fp:
        line=line.strip()
        w=convertLine(line)
        fp1.write(w)
        fp1.write('\n')
    fp.close()
    fp1.close()

if __name__ == '__main__':
    pass