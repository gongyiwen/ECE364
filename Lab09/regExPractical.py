#! /usr/bin/env python3.4
import copy
from sys import *
import os
import re

__author__ = 'ee364e03'

def getNumber(stringInput):
    pattern=r"\+?\d\.\d*[eE][\+\-]?[0-9]*"
    if re.search(pattern,stringInput):
        m=re.search(pattern,stringInput)
        #if len(m.group(2)) >=2:
        #    return None
        out=m.group(0)
        return out
    else:
        return None



def getOptions(commandline):
    pattern=r"-([a-z])\s+([^\s\-]+)\s*"
    list=re.findall(pattern,commandline)
    list.sort()
    return list

def getAddressParts(url):
    pattern=r"^(http\:\/\/|https\:\/\/)(.*?)\/([^\.\_\/]+)?\/([^\/\.]+)"
    if re.match(pattern,url):
        m=re.match(pattern,url)
        if len(m.group(0)) != len(url):
            return None
        print(m.group(0))
        base=m.group(2)
        contro=m.group(3)
        action=m.group(4)
        return (base,contro,action)
    else:
        return None

def getAttributes(xmlSnippet):
    pattern=r"<[a-zA-Z]+\s*(([a-zA-Z]+)\=\"(.*?)\"\s*)(([a-zA-Z]+)\=\"(.*?)\"\s*)(([a-zA-Z]+)\=\"(.*?)\"\s*)\/>"
    if re.match(pattern,xmlSnippet):
        m=re.match(pattern,xmlSnippet)
        tupleA=(m.group(2),m.group(3))
        tupleB=(m.group(5),m.group(6))
        tupleC=(m.group(8),m.group(9))
        st=[]
        st.append(tupleA)
        st.append(tupleB)
        st.append(tupleC)
        st.sort()
        return st
    else:
        return None




if __name__ == '__main__':
    pass
