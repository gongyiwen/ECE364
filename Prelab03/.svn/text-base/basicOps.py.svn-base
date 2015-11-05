#! /usr/bin/env python3.4
__author__ = 'ee364e03'
import sys
import os
import math
import string


def addNumbers(num):
    return sum(range(num+1))

def addMultiplesOf(num):
    return sum(range(0,1001,num))

def getNumberFrequency(num):
    count = 0
    string1 = "The value of Pi is 3 . 1 4 1 5 9 2 6 5 3 5 8 9 7 9 3 2 3 8 4 6 2 6 4 3 3 8 3 2 7 9 5 0 2 8 8 4 1 9 7 1 6 9 3 9 9 3 7 5 1 0 5 8 2 0 9 7 4 9 4 4 5 9 2 3 0 7 8 1 6 4 0 6 2 8 6 2 0 8 9 9 8 6 2 8 0 3 4 8 2 5 3 4 2 1 1 7 0 6 7 9 8 2 1 4 8 0 8 6 5 1 3 2 8 2 3 0 6 6 4 7 0 9 3 8 4 4 6 0 9 5 5 0 5 8 2 2 3 1 7 2 5 3 5 9 4 0 8 1 2 8 4 8 1"
    list = string1.split()
    for item in list:
        if item == str(num):
            count+=1
    return count

def getDigitalSum(string):
    '''
    length = len(string)
    num = int(string)
    sum = 0
    ind = 1
    digit = 0
    while ind <= length:
        digit = num % (math.pow(10,ind))
        power = ind-1
        num -= digit
        sum += digit / (math.pow(10,power))
        ind += 1'''
    sum=0
    for item in string:
        num=int(item)
        sum+=num
    return sum


def getSequenceWithoutDigit(digit):

    strList = ["736925233695599303035509581762617623184956190649483967300203776387436934399982",

"943020914707361894793269276244518656023955905370512897816345542332011497599489",

"627842432748378803270141867695262118097500640514975588965029300486760520801049",

"153788541390942453169171998762894127722112946456829486028149318156024967788794",

"981377721622935943781100444806079767242927624951078415344642915084276452000204",

"276947069804177583220909702029165734725158290463091035903784297757265172087724",

"474095226716630600546971638794317119687348468873818665675127929857501636341131"]
    whole="".join(strList)
    lists=whole.split(str(digit))
    maxlength=0
    maxitem=""
    for item in lists:
        length=len(item)
        if length > maxlength:
            maxlength=length
            maxitem=item
    return maxitem


def capitalizeMe(string):
 '''   words=string.split()
    newword=[]
    newitem=[]
    for item in words:
        length=len(item)
        last=length-1
        count=0
        for ch in item:
            if count == 0 or count == last:
                ch= ch.upper()
            count+=1
            newitem = newitem + [ch]
        newword =" ".join(newitem)
    newstring=" ".join(newword)'''
# string=string.title()
 return ' '.join(word[:len(word)-1] + word[len(word)-1].upper() for word in string.title().split())

if __name__ == '__main__':
    pass
