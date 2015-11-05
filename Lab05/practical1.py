#! /usr/bin/env python3.4
__author__ = 'ee364e03'

def getCallersOf(phoneNumber):
    A={}
    B=[]
    n=0
    with open('Students.txt','r') as myFile:
        all_lines=myFile.readlines()
        all_lines=all_lines[2:]
        for line in all_lines:
            name,num=line.split("|")
            name = name.rstrip()
            num = num.strip()[1:]
            A[num]=name
        with open('Call Log.txt','r') as myFile1:
            all_lines=myFile1.readlines()
            all_lines=all_lines[2:]
            for line in all_lines:
                _,from1,_,to1,time=line.split()
                from2=from1.split("-")[1]
                to2=to1.split("-")[1]
                if to2 == phoneNumber[10:]:
                    if A.get(from2) in B:
                       n=n+1
                    else:
                       if A.get(from2)!= None:
                        name=A.get(from2)

                        B.append(name)

            B.sort()
    return B

def getCallActivity():
    A={}
    B={}
    with open('Students.txt','r') as myFile:
        all_lines=myFile.readlines()
        all_lines=all_lines[2:]
        for line in all_lines:
            name,num=line.split("|")
            name = name.rstrip()
            num = num.strip()[1:]
            A[num]=name
    with open('Call Log.txt','r') as myFile1:
        all_lines=myFile1.readlines()
        all_lines=all_lines[2:]

        for user in A.keys():
            sums=0
            summ=0
            sumh=0
            calltime=0
            for line in all_lines:
                _,from1,_,to1,time=line.split()
                from2=from1.split("-")[1]
                if from2 == user:
                    calltime+=1
                    st1="00:"
                    time=st1+time
                    hh,mm,ss=time.split(":")
                    sums+=int(ss)
                    summ+=int(mm)
                    sumh+=int(hh)
                    if sums >= 60:
                        summ+=1
                        sums-=60
                    if summ >= 60:
                        summ-=60
                        sumh+=1
            C=[calltime,"{0:02d}:{1:02d}:{2:02d}".format(sumh,summ,sums)]
            B[A[user]]=tuple(C)
    return B







if __name__ == '__main__':
    pass
