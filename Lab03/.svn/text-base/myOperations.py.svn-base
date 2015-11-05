#! /usr/bin/env python3.4
__author__ = 'ee364e03'


def checkTypes(l):#takes in a list
    if type(l) != type([1,2,3]):
        return None
    if len(l) == 0:
        return None
    i=0
    f=0
    s=0
    for item in l:
        if type(item) == type(5):
            i=i+1
        elif type(item) == type(2.01):
            f=f+1
        else:
            s=s+1
    g=[i,f,s]
    return g

def normalizeVector(vector):
    if type(vector) != type([1,2,3]):
        return None
    if len(vector) == 0:
        return None
    sum1=sum(vector[0:])
    ind=0
    for item in vector:
        vector[ind]=item/sum1
        ind+=1
    return vector

def findMedian(vList):
    if type(vList) != type([1,2,3]):
        return None
    if len(vList) == 0:
        return None
    for item in vList:
        if (type(item) != type(1)) & (type(item) != type(1.0)):
            return None
    length=len(vList)
    vList.sort()
    median=0
    if length % 2 == 1:
        median = vList[int((length-1)/2)]
    elif length % 2 == 0:
        median = (vList[int(length/2)]+vList[int(length/2 -1)])/2
    return median

def rectifySignal(signal):
    if type(signal) != type([1,2,3]):
        return None
    if len(signal) == 0:
        return None
    ind=0
    for item in signal:
        if item <0:
            signal[ind]=0
        ind+=1
    return signal

def convertToBoolean(num):
    if type(num) != type(1):
        return None
    if (num > 255) | (num < 0):
        return None
    binary=bin(num)
    binary=binary.split('b')
    Boolea=binary[1]
    st=[False,False,False,False,False,False,False,False]
    ind=8-len(Boolea)
    for item in Boolea:
        if item == '1':
            st[ind]= True
        else:
            st[ind]= False
        ind+=1
    return st

def convertToInteger(boolList):

    if type(boolList) != type([1,2,3]):
        return None
 #   if type(boolList) == type([True, 0, 1, False]):
 #       return None
    if len(boolList) == 0:
        return None
    ind = 0
    st=""

    for item in boolList:
        if type(item) != type(True):
            return None
        if item == False:
            boolList[ind] = '0'
        elif item == True:
            boolList[ind] = '1'
        st=st+boolList[ind]
        ind+=1
    st=int(st,2)

    return st

def switchNames(nameList):
    if type(nameList) != type([1,2,3]):
        return None
    if len(nameList) == 0:
        return None
    new=[]
    for item in nameList:
        lastname=item.split(",")[0]
        firstname=item.split(",")[1]
        firstname=firstname.split()[0]
        name=firstname+" "+lastname
        new.append(name)
    return new


def getWeightAverage(data):
    if type(data) != type([1,2,3]):
        return None
    if len(data) == 0:
        return None
    number=len(data)
    sum=0
    for item in data:
        weight=float(item.split()[2])
        sum += weight
    average=sum/number

    return average













if __name__ == '__main__':
    pass
