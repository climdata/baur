# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 13:54:41 2019

@author: Michael Kahle
"""

import codecs
fileName1='baur_yearly.csv'
fileName2='baur_monthly.csv'

months = ['jan','feb','mar','apr','mai','jun','jul','aug','sep','oct','nov','dec']
baurData = {}

with open(fileName1, "r") as ins:
    i=0
    firstLine=""
    for line in ins:
        i=i+1
        #array.append(line)
        #print(line)
        if (1==i):
            firstLine = line
            #print(firstLine)
            header = line.split(';')
        if(i>1):
            #print(line)
            item = {}
            data = line.split(';')
            lineData = {'jan':'','feb':'','mar':'','apr':'','mai':'','jun':'','jul':'','aug':'','sep':'','oct':'','nov':'','dec':''}
            i = 0
            for column in data:
              label = header[i]
              value = data[i]
              lineData[label] = value
              i += 1
            #print(lineData) 
            baurData[lineData['year']] = lineData
  

csvfile2 = codecs.open(fileName2, "w", "utf-8")
csvfile2.write("year;month;m;temperature\n")
for year in baurData:
 m=1   
 for month in months:
   csvfile2.write(year+";"+str(m)+";"+month+";"+baurData[year][month]+"\n") 
   m+=1
csvfile2.close()             