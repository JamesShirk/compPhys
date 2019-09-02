# Declare Libraries
library(ggplot2)
library(scales)
library(pracma)

# Allow the ability to input command line arguments e.g., Rscipt TaylorCosApproximation.R 1 would make args[1] = '1'
args <- commandArgs(trailingOnly = TRUE)

# For a given input 'order' returns the the order of the taylor series for that given order
# Coefs calculates the coefficients for each element of the series
# 

taylor = function(x, order) {
  coefs = (-1)^(0:order) / factorial(2 * (0:order))
  x_grid = outer(x, 2 * (0:order), "^")
  x_grid %*% coefs
}

cosine <- function(x) {
    base::cos(x)
}

plot0 <- ggplot(data = data.frame(x = 0), mapping = aes(x = x)) +
    stat_function(fun = taylor, geom = "line", args = list(order = strtoi(args[1])), mapping = aes(color = "taylor")) +
    stat_function(fun = cosine, geom = "line", linetype = "dashed", mapping = aes(color = "cosine")) +
    scale_x_continuous(limits = c(-pi/2, pi/2)) +
    scale_color_manual(name = "Functions", values = c("taylor" = "#FF0000", "cosine" = "#0000FF"), labels = c("cos(x)", paste("order", strtoi(args[1]) + 1,"\ntaylor approx"))) +
    theme_bw() +
    labs(x = "x", y = "y", title = paste("Order", strtoi(args[1]) + 1, "Taylor Cosine Approximation")) 

ggsave(paste0("taylorCosine",args[1],".png"), plot = plot0, device = NULL, path = NULL,
    scale = 1, width = 20, height = 10, units = c("cm"),
    dpi = 300, limitsize = TRUE)

print(integrate((taylor - cosine), lower = -pi/2, upper = pi/2))