#! /usr/bin/env python3.4
import copy
from sys import *
import os
import re

__author__ = 'ee364e03'

class Duration:
    def __init__(self,hours=0,minutes=0,seconds=0):
        if type(hours) != type(1):
            raise TypeError
        if type(minutes) != type(1):
            raise TypeError
        if type(seconds) != type(1):
            raise TypeError
        if hours < 0:
            raise ValueError
        if minutes < 0:
            raise ValueError
        if seconds < 0:
            raise ValueError
        if seconds >=60:
            minutes+=seconds//60
            seconds%=60
        if minutes >= 60:
            hours+=minutes//60
            minutes%=60
        self.hours=hours
        self.minutes=minutes
        self.seconds=seconds
        self._totalSeconds=hours*3600+minutes*60+seconds

    def __str__(self):
        st='{:02d}:{:02d}:{:02d}'.format(self.hours,self.minutes,self.seconds)
        return st

    def getTotalSeconds(self):
        ts=0
        ts=self.hours*3600+self.minutes*60+self.seconds
        #print(ts)
        return ts

    def __add__(self, other):
        if not isinstance(other,Duration):
            raise TypeError
        else:
            totals=self.seconds+other.seconds
            totalm=self.minutes+other.minutes
            totalh=self.hours+other.hours
            if totals >=60:
                totalm+=totals//60
                totals%=60
            if totalm >= 60:
                totalh+=totalm//60
                totalm%=60
            A=Duration(totalh,totalm,totals)
            return A

    def __mul__(self, other):
        if type(other) != type(1):
            raise TypeError
        elif other <= 0:
            raise ValueError
        else:
            se=self.seconds*other
            mi=self.minutes*other
            ho=self.hours*other
            if se >=60:
                mi+=se//60
                se%=60
            if mi >= 60:
                ho+=mi//60
                mi%=60
            A=Duration(ho,mi,se)
            return A

    def __rmul__(self, other):
        return self.__mul__(other)







if __name__ == '__main__':
    pass

