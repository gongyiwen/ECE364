#! /usr/bin/env python3.4
import copy
__author__ = 'ee364e03'


class Course:
    def __init__(self,courseID,fst,snd,final):
        self.courseID=courseID
        self.fst=fst
        self.snd=snd
        self.final=final
        self.total=0.25*self.fst+0.25*self.snd+0.5*self.final
        if self.total >= 90:
            self.letter='A'
        elif self.total >=80:
            self.letter='B'
        elif self.total >= 70:
            self.letter='C'
        elif self.total >= 60:
            self.letter='D'
        else:
            self.letter='F'


    def __str__(self):
        strrep=self.courseID
        strrep=strrep+': ('+ str(format(self.fst,'.2f'))+', '+str(format(self.snd,'.2f'))+', '+str(format(self.final,'.2f'))+') = ('+str(format(self.total,'.2f'))+', '+self.letter+')'
        return strrep

    def getLetterGrade(self):
        return self.letter

class Student:
    def __init__(self,name):
        self.name=name
        self.courses={}

    def addCourse(self,course):
        if course.courseID in self.courses:
            self.courses[course.courseID]=course
        else:
            self.courses[course.courseID]=course

    def __str__(self):

        strlist=[]
        b=''
        strrep=self.name+':'
        for keys in self.courses.keys():
            id= self.courses[keys]
            a=" ("+ id.courseID + ": " + id.letter + ')'
            strlist.append(a)

        strlist.sort()
        for id in strlist:
            b=b+id+','
        strrep=strrep+b
        strrep=strrep[:-1]
        return strrep


    def generateTranscript(self):
        courselist=[]
        for keys in self.courses.keys():
            id=self.courses[keys]
            a=str(id)
            a='\n'+a
            courselist.append(a)
        courselist.sort()
        strrep=self.name
        for id in courselist:
            strrep=strrep+id
        return strrep

class School:
    def __init__(self,name):
        self.name=name
        self.students={}

    def __str__(self):
        namelist=[]
        strrep=''
        for keys in self.students.keys():
            namelist.append(keys)
        namelist.sort()
        for i in namelist:
            strrep=strrep+'\n'+i
        a=self.name+': '+ str(len(self.students))+' Students'
        strrep=a+strrep
        return strrep

    def loadData(self,filename):
        with open(filename,'r') as myFile:
            all_lines=myFile.read()
            a=all_lines.split("\n\n")
            for lines in a:
                line=lines.split('\n')
                student=Student(line[0])
                courseline=line[2:]
                for course in courseline:
                    courseID=course.split(':')[0][4:]
                    fst=course.split(',')[0][12:]
                    snd=course.split(',')[1][1:]
                    final=course.split(',')[2][1:]
                    courseA=Course(courseID,float(fst),float(snd),float(final))
                    student.addCourse(courseA)
                self.students[student.name]=student




    def saveData(self,filename):
        namelist=[]
        names=[]
        strrep=''
        for keys in self.students.keys():
            names.append(keys)
        names.sort()
        for name in names:
            namelist.append(self.students[name])
        for name in namelist:
            a=name.generateTranscript()
            print(a)
            strrep=strrep+ a+'\n\n'
        strrep=strrep[:-2]
        with open(filename,'w') as myFile:
            myFile.write(strrep)



if __name__ == '__main__':
    pass