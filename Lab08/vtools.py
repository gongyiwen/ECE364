#! /usr/bin/env python3.4
import copy
from sys import *
import os
import re

__author__ = 'ee364e03'

def isValidName(identifier):
    pattern=r"\w+"
    if re.match(pattern,identifier):
        m=re.match(pattern,identifier)
        if len(m.group(0)) == len(identifier):
            return True
        else:
            return False
    else:
        return False



def parsePinAssignment(assignment):
    pattern=r"\s*\.\w+\(\w+\)\s*"
    if re.match(pattern,assignment):
        a=re.match(pattern,assignment)
        if len(a.group(0)) < len(assignment):
            raise ValueError(assignment)
        assignment1=assignment.split('(')
        portname=assignment1[0].split('.')[1]
        pinname=assignment1[1].split(')')[0]
        m=isValidName(portname)
        n=isValidName(pinname)
        if m & n:
            b=(portname,pinname)
            return b
        else:
            raise ValueError(assignment)
    else:
        raise ValueError(assignment)




def parseNetLine(line):
    pattern=r"\s*(\w+)\s+(\w+)\s*(\(){1}([\.\s*\w+\(\w+\)\,]+)\s*\)"
    if re.match(pattern,line):
        m=re.match(pattern,line)
        comp_name=m.group(1)
        #print(comp_name)
        if isValidName(comp_name) == False:
            raise ValueError(line)
        ins_name=m.group(2)
        #print(ins_name)
        if isValidName(ins_name)==False:
            raise ValueError(line)
        assignmentlist=m.group(4)
        #print(assignmentlist)
        if len(m.group(0)) != len(line):
            raise ValueError(line)
        assignmentlist1=assignmentlist.split(',')
        #print(assignmentlist1)
        pattern1=r"\(\."
        if re.match(pattern1,assignmentlist1[0]):
            #print(1)
            raise ValueError(line)

        n=0
        a=[]
        for item in assignmentlist1:
            c=parsePinAssignment(item)
            a.append(c)
        a=tuple(a)
        if n==0:
            b=(comp_name,ins_name,a)
            return b
    else:
        raise ValueError(line)

    #print(line1)
    #comp_name=line1[0]
    #instance_name=line1[1]
    #assignment_list=line1[2:]
    #print(comp_name)
    #print(instance_name)
    #print(assignment_list)




if __name__ == '__main__':
    pass