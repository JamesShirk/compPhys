library(ggplot2)
library(scales)
library(pracma)

taylor0 <- function(x) {
    1
}

taylor4 <- function(x) {
    (1-((x**2)/2)+((x**4)/24)-((x**6)/720))
    }

taylor8 <- function(x) {
    (1-((x**2)/2)+((x**4)/24)-((x**6)/720)+((x**8)/40320)-((x**10)/3628800)+((x**12)/479001600)-((x**14)/87178291200))#+((x**16)/20922789888000‬)-((x**18)/6402373705728000))
}

f0cos <- function(x) {
    (1 - base::cos(x))
    }

f4cos <- function(x) {
    (1-((x**2)/2)+((x**4)/24)-((x**6)/720) - base::cos(x))
    }

f8cos <- function(x) {
    (1-((x**2)/2)+((x**4)/24)-((x**6)/720)+((x**8)/40320)-((x**10)/3628800)+((x**12)/479001600)-((x**14)/87178291200) - base::cos(x))
    }

cosine <- function(x) {
    base::cos(x)
    }

plot0 <- ggplot(data = data.frame(x = 0), mapping = aes(x = x)) +
    stat_function(fun = taylor0, geom = "line", mapping = aes(color = "taylor0")) +
    stat_function(fun = cosine, geom = "line", mapping = aes(color = "cosine")) +
    scale_x_continuous(limits = c(-pi, pi)) +
    scale_color_manual(name = "Functions", values = c("taylor0" = "#FF0000", "cosine" = "#0000FF"), labels = c("cos(x)", "Leading order \ntaylor approx")) +
    theme_bw() +
    labs(x = "x", y = "y", title = "Fourth Order Taylor Cosine Approximation") 

plot1 <- ggplot(data = data.frame(x = 0), mapping = aes(x = x)) +
    stat_function(fun = taylor4, geom = "line", mapping = aes(color = "taylor4")) +
    stat_function(fun = cosine, geom = "line", mapping = aes(color = "cosine")) +
    scale_x_continuous(limits = c(-pi, pi)) +
    scale_color_manual(name = "Functions", values = c("taylor4" = "#FF0000", "cosine" = "#0000FF"), labels = c("cos(x)", "Fourth order \ntaylor approx")) +
    theme_bw() +
    labs(x = "x", y = "y", title = "Fourth Order Taylor Cosine Approximation") 

plot2 <- ggplot(data = data.frame(x = 0), mapping = aes(x = x)) +
    stat_function(fun = taylor8, geom = "line", mapping = aes(color = "taylor8")) +
    stat_function(fun = cosine, geom = "line", mapping = aes(color = "cosine")) +
    scale_x_continuous(limits = c(-pi, pi)) +
    scale_color_manual(name = "Functions", values = c("taylor8" = "#FF0000", "cosine" = "#0000FF"), labels = c("cos(x)", "Eighth order \ntaylor approx")) +
    theme_bw() +
    labs(x = "x", y = "y", title = "Fourth Order Taylor Cosine Approximation") 

ggsave("cosineTaylor0.png", plot = plot0, device = NULL, path = NULL,
  scale = 1, width = 20, height = 10, units = c("cm"),
  dpi = 300, limitsize = TRUE)

ggsave("cosineTaylor3.png", plot = plot1, device = NULL, path = NULL,
  scale = 1, width = 20, height = 10, units = c("cm"),
  dpi = 300, limitsize = TRUE)

ggsave("cosineTaylor8.png", plot = plot2, device = NULL, path = NULL,
  scale = 1, width = 20, height = 10, units = c("cm"),
  dpi = 300, limitsize = TRUE)

print(integrate(f0cos, lower = -pi, upper = pi))
print(integrate(f4cos, lower = -pi, upper = pi))
print(integrate(f8cos, lower = -pi, upper = pi))
