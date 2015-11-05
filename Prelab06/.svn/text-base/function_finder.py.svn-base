#! /usr/bin/env python3.4
import re
import sys
import os
__author__ = 'ee364e03'


def funccheck():

    if num != 2:
        print("Usage: function_finder.py [python_file_name]")
        return
    elif os.path.exists(filename) == False:
        print("Error: {} does not exist".format(filename))
        return
    elif os.access(filename, os.R_OK)== False:
        print("Error: Could not read {}".format(filename))
        return
    else:
        pattern_search()
        return


def pattern_search():
        pattern=r"def\s*([\w-]*)\s*\(([\w,\s=-]+)\)\:"
        with open(filename,'r') as myFile:
            all_lines=myFile.readlines()
            for line in all_lines:
                if re.search(pattern,line):
                    m=re.search(pattern,line)
                    print(m.group(1))
                    m1=m.group(2).split(",")
                    count=1
                    for item in m1:
                        item1=item.strip()
                        print('Arg{}: {}'.format(count,item1))
                        count+=1




if __name__ == '__main__':
    filename = sys.argv[1]
    num=len(sys.argv)
    funccheck()








