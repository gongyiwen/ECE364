#! /usr/bin/env python3.4
from sys import *
import os
import re
#import Pillow
import numpy as np
import scipy.misc
from enum import Enum


__author__ = 'ee364e03'

class Effect(Enum):
    rotate90=1
    rotate180=2
    rotate270=3
    flipHorizontally=4
    flipVertically=5
    transpose=6


class Homography:
    def __init__(self,**kwargs):
        #if the parameter passed has a different name
        name=('homographyMatrix','sourcePoints','targetPoints','effect')
        found=1
        for i in kwargs:
            if i not in name:
                found=0
        if 'homographyMatrix' in kwargs:
            self.matrix = kwargs['homographyMatrix']
            if len(self.matrix) != 3: # column
                raise ValueError ("matrix is not 3*3")
            if len(self.matrix) !=3: # row
                raise ValueError ("matrix is not 3*3")# if the matrix is not of size 3*3
            for i in self.matrix:
                for j in i:
                    if type(j)!=type(1.0):
                        raise ValueError ("type of value in matrix is not float")# if the values are not fo type float
        if 'sourcePoints' in kwargs:
            self.sourcePoint=kwargs['sourcePoints']
            if len(self.sourcePoint) !=4:
                    raise ValueError("Bad point")
            #for i in self.sourcePoint:
            #            if type(i[0]) != type(1.0) or type(i[1]) != type(1.0):
            #                raise ValueError("type of value in sourcepoint is not float")
        if 'targetPoints' in kwargs:
            self.targetPoint=kwargs['targetPoints']
            if len(self.targetPoint) !=4:
                    raise ValueError("Bad point")
            #for i in self.targetPoint:
             #           if type(i[0]) != type(1.0) or type(i[1]) != type(1.0):
            #                raise ValueError("type of value in targetpoint is not float")
        if 'effect' in kwargs:
            effect=kwargs['effect']
            if not isinstance(effect,Effect) and effect != None:
                raise TypeError
        if found ==0:
            raise ValueError ('key is not correct')

    def forwardProject(self,point):
        self.matrix=self.computeHomography(self.sourcePoint,self.targetPoint)

        #apply the homography to the given (x,y) point, and return the point (x',y'). This method takes in and
        #returns a two-element tuple.
        print(self.matrix)
        x=point[0]
        y=point[1]
        point1=np.array([x,y,1])
        point1=np.resize(point1,(3,1))
        print(point1)
        resultpoint=self.matrix.dot(point1)
        result=(resultpoint[0][0],resultpoint[1][0])
        print(resultpoint)
        return result

    def inverseProject(selfself,pointPrime):
        #Apply the inverse homography to the given (x',y') point, and return the point (x, y).
        # This method takes in and returns a two element tuple.
        pass

    def computeHomography(self,sourcePoints,targetPoints,effect=None):
        A=np.array([])
        b=np.array([])
        for i,j in zip(sourcePoints,targetPoints):
            x1=i[0]
            y1=i[1]
            x2=j[0]
            y2=j[1]
            b=np.append(b,x2)
            b=np.append(b,y2)
            B=np.array([x1,y1,1,0,0,0,-x2*x1,-x2*y1])
            C=np.array([0,0,0,x1,y1,1,-y2*x1,-y2*y1])
            A=np.append(A,B,axis=0)
            A=np.append(A,C,axis=0)

        A=np.resize(A,(8,8))
        b=np.resize(b,(8,1))
        #print('A={}'.format(A))
        #print('b={}'.format(b))
        h=np.linalg.solve(A,b)
        h=np.append(h,1)
        h=np.resize(h,(3,3))
        return h





class Transformation:
    def __init__(self,sourceImage,homography=None):
        #Initialize an instance of the Transformation class using a specific sourceImage, which is an instance of
        # ndarray and a homography instance.Raise aTypeError with an appropriate message if either of the parameters
        # is not an instance of the correct type
        self.a=scipy.misc.imread(sourceImage,True)
        self.targetPoints=0
        self.sourcePoints=0


    def setupTransformation(self, targetPoints, effect=None):
        self.targetPoints=targetPoints
        #Takes in target Points, a list of 4 elements, each of which is a point tuple.  These points can be used
        # to identify the range of iteration in the target image

        pass
    def transformImage(self, containerImage):

        pass

class ColorTransformation(Transformation):
    def __init__(self,sourceImage, homography=None):
        Transformation.__init__(self,sourceImage,homography)
        pass

    def transformImage(self, containerImage):
        pass

class AdvancedTransformation:
    def __init__(self,sourceImage,v,h1,h2):
        pass
    def applyEffectV(self):
        pass
    def applyEffectA(self):
        pass





if __name__ == "__main__":

    p = 70.0, 80.0
    s = [(0.0, 0.0), (150.0, 0.0), (0.0, 200.0), (150.0, 200.0)]
    h = Homography(sourcePoints=s, targetPoints=s, effect=Effect.rotate180)

    expected1, expected2 = 80.0, 120.0
    actual1, actual2 = h.forwardProject(p)
    print(actual1,actual2)
    #h = Homography(sourcePoints=s, targetPoints=t)
    #b=h.forwardProject(p)
    #a=h.computeHomography(s,t)