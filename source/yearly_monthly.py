# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 13:54:41 2019

@author: Michael Kahle
"""

import codecs
fileName1='./raw/baur_yearly.csv'
fileName2='./raw/baur_monthly.csv'

months = ['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']
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
            header = line.split(',')
        if(i>1):
            #print(line)
            item = {}
            data = line.split(',')
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
csvfile2.write("year,month,time,ts,m,temperature\n")
for year in sorted(baurData):
 m=1   
 for month in months:
   time = float(year)+(m-0.5)/12.0
   csvfile2.write(year+","+str(m)+","+year+"-"+str(m)+"-15 00:00:00"+","+str(time)+","+month+","+baurData[year][month]+"\n") 
   m+=1
csvfile2.close()             