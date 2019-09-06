library(ggplot2)
library(scales)

z <- data.frame(N=integer(), Difference=double(), stringsAsFactors=FALSE)

taylor = function(x, order) {
  coefs = (-1)^(0:order) / factorial(2 * (0:order))
  x_grid = outer(x, 2 * (0:order), "^")
  x_grid %*% coefs
}

cosine = function(x) {
    base::cos(x)
}

taylorCosine = function(x, order){
  coefs = (-1)^(0:order) / factorial(2 * (0:order))
  x_grid = outer(x, 2 * (0:order), "^")
  base::cos(x) - (x_grid %*% coefs)
}
for (i in 0:9){
    taylorInt = integrate(taylor, lower = -pi/2, upper = pi/2, order = i)
    cosineInt = integrate(cosine, lower = -pi/2, upper = pi/2)
    percentDifference = abs(((taylorInt$value - cosineInt$value)/cosineInt$value)*100)
    z[(i + 1),1] <- (i)
    z[(i + 1),2] <- (percentDifference)
}

plot0 <- ggplot(data=z, aes(x=N, y=Difference, group=1)) +
    geom_point(color = "#FF0000") +
      geom_smooth(method = "lm", se = FALSE) +
    theme_bw() +
    labs(x = "Order", y = "Percent Difference", title = "Percent Difference over Order") +
    scale_y_continuous(trans='log10') +
    scale_x_continuous(breaks=seq(0,10,1))

ggsave("orderDifference.png", plot = plot0, device = NULL, path = NULL,
  scale = 1, width = 20, height = 10, units = c("cm"),
  dpi = 300, limitsize = TRUE)