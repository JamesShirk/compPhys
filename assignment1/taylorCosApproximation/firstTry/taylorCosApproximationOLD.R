# James Shirk, August 27-29, 2019 for Dr. Pratt Computational Physics class assignment 1, problem 2

library(ggplot2)
library(scales)
library(pracma)

taylorOrder0 <- read.table(file="taylorOutputOrder0.txt", head=FALSE, sep=",")
taylorOrder3 <- read.table(file="taylorOutputOrder3.txt", head=FALSE, sep=",")
taylorOrder9 <- read.table(file="taylorOutputOrder9.txt", head=FALSE, sep=",")
taylorOrder50 <- read.table(file="taylorOutputOrder50.txt", head=FALSE, sep=",")
numbers <- read.table(file="numberList.txt", head=FALSE)

y <- cos(numbers)

cosine <- data.frame(numbers,y)
taylorSeries0 <- data.frame(numbers,taylorOrder0)
taylorSeries3 <- data.frame(numbers,taylorOrder3)
taylorSeries9 <- data.frame(numbers,taylorOrder9)
taylorSeries50 <- data.frame(numbers,taylorOrder50)

error0 = merge(cosine, taylorSeries0, by = "V1")
colnames(error0) <- c("numbers","taylor0","cosine")
error0[ ,4] <- error0$cosine - error0$taylor0
error0[ ,4] <- error0[ ,4] / error0$cosine
error0[ ,4] <- error0[ ,4] * 100
cat("The mean error of the leading order is: ",mean(error0[ ,4]), "%\n")

error3 = merge(cosine, taylorSeries3, by = "V1")
colnames(error3) <- c("numbers","taylor3","cosine")
error3[ ,4] <- error3$cosine - error3$taylor3
error3[ ,4] <- error3[ ,4] / error3$cosine
error3[ ,4] <- error3[ ,4] * 100
cat("The mean error of the fourth order is: ",mean(error3[ ,4]), "%\n")

error9 = merge(cosine, taylorSeries9, by = "V1")
colnames(error9) <- c("numbers","taylor9","cosine")
error9[ ,4] <- error9$cosine - error9$taylor9
error9[ ,4] <- error9[ ,4] / error9$cosine
error9[ ,4] <- error9[ ,4] * 100
cat("The mean error of the tentth order is: ",mean(error9[ ,4]), "%\n")

error50 = merge(cosine, taylorSeries9, by = "V1")
colnames(error50) <- c("numbers","taylor9","cosine")
error50[ ,4] <- error50$cosine - error50$taylor9
error50[ ,4] <- error50[ ,4] / error50$cosine
error50[ ,4] <- error50[ ,4] * 100
cat("The mean error of the fifty-first order is: ",mean(error50[ ,4]), "%\n")

cosineTaylor0 <- ggplot() +
    geom_line(data=cosine, aes(x=V1, y=V1.1, group=1, colour="#FF0000")) +
    geom_line(data=taylorSeries0, aes(x=V1, y=V1.1, group=1, colour="#0000FF")) +
    scale_color_discrete(name = "Comparison", labels = c("cos(x)", "Leading Order Taylor Approx")) +
    geom_hline(yintercept = 0) +
    theme_bw() +
    labs(x = "x", y = "y", title = "Leading Order Taylor Cosine Approximation") 

cosineTaylor3 <- ggplot() +
    geom_line(data=cosine, aes(x=V1, y=V1.1, group=1, colour="#FF0000")) +
    geom_line(data=taylorSeries3, aes(x=V1, y=V1.1, group=1, colour="#0000FF")) +
    scale_color_discrete(name = "Comparison", labels = c("cos(x)", "Fourth Order Taylor Approx")) +
    geom_hline(yintercept = 0) +
    theme_bw() +
    labs(x = "x", y = "y", title = "Fourth Order Taylor Cosine Approximation") 

cosineTaylor9 <- ggplot() +
    geom_line(data=cosine, aes(x=V1, y=V1.1, group=1, colour="#FF0000")) +
    geom_line(data=taylorSeries9, aes(x=V1, y=V1.1, group=1, colour="#0000FF")) +
    scale_color_discrete(name = "Comparison", labels = c("cos(x)", "Tenth Order Taylor Approx")) +
    geom_hline(yintercept = 0) +
    theme_bw() +
    labs(x = "x", y = "y", title = "Tenth Order Taylor Cosine Approximation") 

cosineTaylor50 <- ggplot() +
    geom_line(data=cosine, aes(x=V1, y=V1.1, group=1, colour="#FF0000")) +
    geom_line(data=taylorSeries50, aes(x=V1, y=V1.1, group=1, colour="#0000FF")) +
    scale_color_discrete(name = "Comparison", labels = c("cos(x)", "Fifty-first Order Taylor Approx")) +
    geom_hline(yintercept = 0) +
    theme_bw() +
    labs(x = "x", y = "y", title = "Fifty-first Order Taylor Cosine Approximation") 

ggsave("cosineTaylor0.png", plot = cosineTaylor0, device = NULL, path = NULL,
  scale = 1, width = 20, height = 10, units = c("cm"),
  dpi = 300, limitsize = TRUE)

ggsave("cosineTaylor3.png", plot = cosineTaylor3, device = NULL, path = NULL,
  scale = 1, width = 20, height = 10, units = c("cm"),
  dpi = 300, limitsize = TRUE)

ggsave("cosineTaylor9.png", plot = cosineTaylor9, device = NULL, path = NULL,
  scale = 1, width = 20, height = 10, units = c("cm"),
  dpi = 300, limitsize = TRUE)

ggsave("cosineTaylor50.png", plot = cosineTaylor50, device = NULL, path = NULL,
  scale = 1, width = 20, height = 10, units = c("cm"),
  dpi = 300, limitsize = TRUE)

