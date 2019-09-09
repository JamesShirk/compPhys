require(splines)

data <- read.csv(file="data.txt", header = TRUE, sep = ",")


png(filename = "test.png")
plot(data$x, data$y, ylim = c(-.4,1.2))
lines(spline(data$x, data$y, n = 1000*length(data)))
dev.off()
