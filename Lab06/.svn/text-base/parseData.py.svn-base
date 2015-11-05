#! /usr/bin/env python3.4
import re
import sys
import os
__author__ = 'ee364e03'

with open('UserData.txt','r') as myFile:
            all_lines=myFile.readlines()

def getInvalidUsers():
    names=[]
    pattern1=r"([A-Za-z]+)(,?)\s([A-Za-z]+)(\s|,)+$"
    for line in all_lines:
        if re.match(pattern1,line):
            m1=re.match(pattern1,line)

            if m1.group(2)==",":
                firstname=m1.group(3)
                lastname=m1.group(1)
                name=firstname+" "+lastname

                names.append(name)
            else:
                firstname=m1.group(1)
                lastname=m1.group(3)
                name=firstname+" "+lastname
                #print(name)
                names.append(name)
    names.sort()

    return names




def getUsersWithEmails():
    C=[]
    pattern1=r"([A-Za-z]+)(,?)\s([A-Za-z]+)(\s|,)+([\w.-]+)@([\w.-]+)(\s|,)+$"
    for line in all_lines:
         if re.match(pattern1,line):
            m1=re.match(pattern1,line)
            #print(m1)
            if m1.group(2)==",":
                firstname=m1.group(3)
                lastname=m1.group(1)
                email=m1.group(5)+"@"+m1.group(6)
                name=firstname+" "+lastname
                A=[]
                A.append(name)
                A.append(email)
                B=tuple(A)
                C.append(B)
            else:
                firstname=m1.group(1)
                lastname=m1.group(3)
                name=firstname+" "+lastname
                email=m1.group(5)+"@"+m1.group(6)
                A=[]
                A.append(name)
                A.append(email)
                B=tuple(A)
                C.append(B)
    C.sort()
    return C

def getUsersWithPhones():
    C=[]
    pattern1=r"([A-Za-z]+)(,?)\s([A-Za-z]+)(\s|,)+\(?([\d]{3})\)?-?\s?([\d]{3})-?([\d]{4})(\s|,)+$"
    for line in all_lines:
         if re.match(pattern1,line):
            m1=re.match(pattern1,line)
            #print(m1)
            if m1.group(2)==",":
                firstname=m1.group(3)
                lastname=m1.group(1)
                phonenumber="("+m1.group(5)+")"+" "+m1.group(6)+"-"+m1.group(7)
                name=firstname+" "+lastname
                A=[]
                A.append(name)
                A.append(phonenumber)
                B=tuple(A)
                C.append(B)
            else:
                firstname=m1.group(1)
                lastname=m1.group(3)
                name=firstname+" "+lastname
                phonenumber="("+m1.group(5)+")"+" "+m1.group(6)+"-"+m1.group(7)
                A=[]
                A.append(name)
                A.append(phonenumber)
                B=tuple(A)
                C.append(B)
    C.sort()
    return C

def getUsersWithStates():
    C=[]
    pattern1=r"([A-Za-z]+)(,?)\s([A-Za-z]+)(\s|,)+((\w+\s\w+)|(\w+))$"
    for line in all_lines:
         if re.match(pattern1,line):
            m1=re.match(pattern1,line)
            #print(m1)
            if m1.group(2)==",":
                firstname=m1.group(3)
                lastname=m1.group(1)
                statename=m1.group(5)
                name=firstname+" "+lastname
                A=[]
                A.append(name)
                A.append(statename)
                B=tuple(A)
                C.append(B)
            else:
                firstname=m1.group(1)
                lastname=m1.group(3)
                name=firstname+" "+lastname
                statename=m1.group(5)
                A=[]
                A.append(name)
                A.append(statename)
                B=tuple(A)
                C.append(B)
    C.sort()
    return C


def getUsersWithEmailsAndPhones():
    C=[]
    pattern1=r"([A-Za-z]+)(,?)\s([A-Za-z]+)(\s|,)+([\w.-]+)@([\w.-]+)(\s|,)+\(?([\d]{3})\)?-?\s?([\d]{3})-?([\d]{4})(\s|,)+$"
    for line in all_lines:
         if re.match(pattern1,line):
            m1=re.match(pattern1,line)
            #print(m1)
            if m1.group(2)==",":
                firstname=m1.group(3)
                lastname=m1.group(1)
                name=firstname+" "+lastname
                email=m1.group(5)+"@"+m1.group(6)
                phone="("+m1.group(8)+")"+" "+m1.group(9)+"-"+m1.group(10)
                A=[]
                A.append(name)
                A.append(email)
                A.append(phone)
                B=tuple(A)
                C.append(B)
            else:
                firstname=m1.group(1)
                lastname=m1.group(3)
                name=firstname+" "+lastname
                email=m1.group(5)+"@"+m1.group(6)
                phone="("+m1.group(8)+")"+" "+m1.group(9)+"-"+m1.group(10)
                A=[]
                A.append(name)
                A.append(email)
                A.append(phone)
                B=tuple(A)
                C.append(B)
    C.sort()
    return C


def getUsersWithEmailsAndStates():
    C=[]
    pattern1=r"([A-Za-z]+)(,?)\s([A-Za-z]+)(\s|,)+([\w.-]+)@([\w.-]+)(\s|,)+((\w+\s\w+)|(\w+))$"
    for line in all_lines:
         if re.match(pattern1,line):
            m1=re.match(pattern1,line)
            #print(m1)
            if m1.group(2)==",":
                firstname=m1.group(3)
                lastname=m1.group(1)
                name=firstname+" "+lastname
                email=m1.group(5)+"@"+m1.group(6)
                state=m1.group(8)
                A=[]
                A.append(name)
                A.append(email)
                A.append(state)
                B=tuple(A)
                C.append(B)
            else:
                firstname=m1.group(1)
                lastname=m1.group(3)
                name=firstname+" "+lastname
                email=m1.group(5)+"@"+m1.group(6)
                state=m1.group(8)
                A=[]
                A.append(name)
                A.append(email)
                A.append(state)
                B=tuple(A)
                C.append(B)
    C.sort()
    return C

def getUsersWithPhonesAndStates():
    C=[]
    pattern1=r"([A-Za-z]+)(,?)\s([A-Za-z]+)(\s|,)+\(?([\d]{3})\)?-?\s?([\d]{3})-?([\d]{4})(\s|,)+((\w+\s\w+)|(\w+))$"
    for line in all_lines:
         if re.match(pattern1,line):
            m1=re.match(pattern1,line)
            #print(m1)
            if m1.group(2)==",":
                firstname=m1.group(3)
                lastname=m1.group(1)
                name=firstname+" "+lastname
                phone="("+m1.group(5)+")"+" "+m1.group(6)+"-"+m1.group(7)
                state=m1.group(9)
                A=[]
                A.append(name)
                A.append(phone)
                A.append(state)
                B=tuple(A)
                C.append(B)
            else:
                firstname=m1.group(1)
                lastname=m1.group(3)
                name=firstname+" "+lastname
                phone="("+m1.group(5)+")"+" "+m1.group(6)+"-"+m1.group(7)
                state=m1.group(9)
                A=[]
                A.append(name)
                A.append(phone)
                A.append(state)
                B=tuple(A)
                C.append(B)
    C.sort()
    return C

def getValidUsers():
    C=[]
    pattern1=r"([A-Za-z]+)(,?)\s([A-Za-z]+)(\s|,)+([\w.-]+)@([\w.-]+)(\s|,)+\(?([\d]{3})\)?-?\s?([\d]{3})-?([\d]{4})(\s|,)+((\w+\s\w+)|(\w+))$"
    for line in all_lines:
         if re.match(pattern1,line):
            m1=re.match(pattern1,line)
            #print(m1)
            if m1.group(2)==",":
                firstname=m1.group(3)
                lastname=m1.group(1)
                name=firstname+" "+lastname
                email=m1.group(5)+"@"+m1.group(6)
                phone="("+m1.group(8)+")"+" "+m1.group(9)+"-"+m1.group(10)
                state=m1.group(12)
                A=[]
                A.append(name)
                A.append(email)
                A.append(phone)
                A.append(state)
                B=tuple(A)
                C.append(B)
            else:
                firstname=m1.group(1)
                lastname=m1.group(3)
                name=firstname+" "+lastname
                email=m1.group(5)+"@"+m1.group(6)
                phone="("+m1.group(8)+")"+" "+m1.group(9)+"-"+m1.group(10)
                state=m1.group(12)
                A=[]
                A.append(name)
                A.append(email)
                A.append(phone)
                A.append(state)
                B=tuple(A)
                C.append(B)
    C.sort()
    return C






if __name__ == '__main__':
    pass