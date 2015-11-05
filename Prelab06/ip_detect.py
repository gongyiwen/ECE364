#! /usr/bin/env python3.4
import re
import sys
__author__ = 'ee364e03'

if __name__ == '__main__':
    filename = sys.argv[1]
    ip=r"(([0-1]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])\.([0-1]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])\.([0-1]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])\.([0-1]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])\:)"
    port=r"([0-3]?[0-9]?[0-9]?[0-9]?[0-9]?)"
    with open(filename,'r') as myFile:
        all_lines=myFile.readlines()
        for line in all_lines:
            if re.search(ip,line):
                m1=re.search(ip,line)
                m2=line.split(":")[1][:-1]
                #print(m2)
                 #if re.search(port,line):
                if re.match(port,m2): #if m1 is int
                    m3=re.match(port,m2)
                    #print(m3.group(0))
                    if m3.group(0) != m2:
                        print(m1.group(0)+str(m2)+ " - Invalid Port Number")
                    else:
                        m3=int(m3.group(0))
                        if (m3 > 1) & (m3 < 32767):
                            if m3 < 1024:
                                print(m1.group(0)+str(m3)+" - Valid (root privileges required)")
                            else:
                                print(m1.group(0)+str(m3)+ " - Valid")
                        else:
                            print(m1.group(0)+str(m3)+ " - Invalid Port Number")
            else:#ip is invalid
                line=line.rstrip()
                print(line + " - Invalid IP Address")







