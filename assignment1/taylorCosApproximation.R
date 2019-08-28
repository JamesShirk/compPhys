# James Shirk, August 27, 2019 for Dr. Pratt Computational Physics class assignment 1, problem 2

library(ggplot2)
library(scales)
library(pracma)

t = seq(0,10,.1)
y = cos(t)

cosine <- data.frame(t,y)
taylorSeries1 <- data.frame(t)


comparisonPlot <- ggplot() +
    geom_line(data=cosine, aes(x=t, y=y, group=1), colour="#FF0000") +
    geom_line(data=taylorSeries, aes(x=t, y=y, group=1), colour="#FF0000") +

