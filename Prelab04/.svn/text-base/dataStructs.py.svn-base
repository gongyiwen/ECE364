#! /usr/bin/env python3.4
__author__ = 'ee364e03'
import glob
import re
filelist = glob.glob('files/*.txt')
purchaselist=glob.glob('purchases/purchase*.txt')
def getWordFrequency():

    A={}
    for item in filelist:
        with open(item,'r') as myFile:
            for line in myFile:
                for word in line.split():
                    if A.get(word) != None:
                        A[word]=A[word]+1
                    else:
                        A[word]=1
    return A


def getDuplicates():
    all_lines=""
    A={}
    B={}
    for item in filelist:
        name=item[6:9]
        with open(item,'r') as myFile:
            #all_lines=myFile.readlines()
            all_lines = myFile.read()
            if A.get(all_lines) !=None:
                A[all_lines].append(name)
            else:
                A[all_lines]=[]
                A[all_lines].append(name)

    for key in A.keys():
        value=A[key]
        key=re.split(r'[^0-9A-Za-z]+',key)
        #for i in range(len(key)):
        #    key[i] = key[i].lower()
        length=len(set(key))-1
        value.sort()
        B[value[0]]=(length,value)
    return B

def getPurchaseReport():
    PriceList={}
    A={}
    with open('purchases/Item List.txt','r') as Price:
        all_lines=Price.readlines()
        all_lines=all_lines[2:]
        for line in all_lines:
            line=line.split()
            PriceList[line[0]]=float(line[1][1:])
    for item in purchaselist:
        name=int(item[19:22])
        with open(item,'r') as a:
            all_lines1=a.readlines()
            all_lines1=all_lines1[2:]
            sum=0.00
            for line1 in all_lines1:
                line1=line1.split()
                q=float(line1[1])
                p=PriceList.get(line1[0])
                sum+=p*q
        A[name]=round(sum,2)
    return A

def getTotalSold():
    A={}
    for item in purchaselist:
        with open(item,'r') as a:
            all_lines=a.readlines()
            all_lines=all_lines[2:]
            for line in all_lines:
                line=line.split()
                q=int(line[1])
                name=line[0]
                if A.get(name) == None:
                    A[name]=q
                else:
                    A[name]+=q
    return A



if __name__ == '__main__':
    pass