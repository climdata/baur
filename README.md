---
title: "Baur"
author: "KMicha71"
date: "2 8 2019"
output:
  html_document: 
    keep_md: true
  pdf_document: default
---



## Baur Serie


Monthly Temperature data of Central Europe (~Germany) as taken from
https://de.wikipedia.org/wiki/Zeitreihe_der_Lufttemperatur_in_Deutschland#Messwerte_in_Dekaden

### Create plain monthly series


```sh
python ./source/yearly_monthly.py
```


```r
#install.packages("ggplot2")
require("ggplot2")
```

```
## Loading required package: ggplot2
```

```
## Warning: package 'ggplot2' was built under R version 3.5.3
```

```r
color.temperature <- c("#0000FF", "#00CCCC", "#FFFFFF", "#EEAA33", "#FF5555")
#setwd(dirname(rstudioapi::getActiveDocumentContext()$path))
py <- read.csv("https://raw.githubusercontent.com/climdata/baur/master/csv/baur_monthly.csv", sep=",")
py2 <- subset(py, !is.na(py$temperature))
```

## Plot Month-Table


```r
mp <- ggplot(py2, aes(year, month))
mp + geom_raster(aes(fill=temperature))+
  scale_y_continuous(breaks=c(1,6,12))+
  theme(panel.background = element_rect(fill = '#EEEEEE', colour = 'white'), legend.position="right", text=element_text(size=14))+
  scale_fill_gradientn(colours=color.temperature)
```

![](README_files/figure-html/monthly-1.png)<!-- -->

## Plot more classical diagram


```r
mp <- ggplot()
jan <- subset(py2, py2$month == 1)
jul <- subset(py2, py2$month == 7)
mp + geom_line(aes(y=jan$temperature, x=jan$year)) + 
     geom_line(aes(y=jul$temperature, x=jul$year))
```

![](README_files/figure-html/classical-1.png)<!-- -->

## Work with yearly


```r
#install.packages("data.table")
library(data.table)
library(zoo)
```

```
## 
## Attaching package: 'zoo'
```

```
## The following objects are masked from 'package:base':
## 
##     as.Date, as.Date.numeric
```

```r
py3 <- read.csv("https://raw.githubusercontent.com/climdata/baur/master/csv/baur_yearly.csv", sep=",")
avg <- rollapply(py3, width=30, by=1, FUN=mean)
#avg$year = py3$year[30:]
#std <- rollapply(py3, width=30, by=1, FUN=stddev)
```
