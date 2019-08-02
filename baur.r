#install.packages("ggplot2")

require("ggplot2")


color.temperature <- c("#0000FF", "#00CCCC", "#FFFFFF", "#EEAA33", "#FF5555")

setwd(dirname(rstudioapi::getActiveDocumentContext()$path))
py <- read.csv("baur_monthly.csv", sep=";")
py2 <- subset(py, !is.na(py$temperature))

hist(py$temperature)

mp <- ggplot(py2, aes(year, month))

mp + geom_raster(aes(fill=temperature))+
  scale_y_continuous(breaks=c(1,6,12))+
  theme(panel.background = element_rect(fill = '#EEEEEE', colour = 'white'), legend.position="right", text=element_text(size=14, family="Calibri"))+
  scale_fill_gradientn(colours=color.temperature)

ggplot(aes(y = temperature, x = year+month/12), data = py2, x)+ 
  labs(fill= "Index", x = "Year", y = "Temperature", title = "")+
}

mp <- ggplot()
jan <- subset(py2, py2$month == 1)
jul <- subset(py2, py2$month == 7)
mp + geom_line(aes(y=jan$temperature, x=jan$year)) + 
     geom_line(aes(y=jul$temperature, x=jul$year))
