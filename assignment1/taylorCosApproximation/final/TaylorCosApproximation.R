# James Shirk, August 30, September 1, 2 2019 for Dr. Pratt Computational Physics class assignment 1, problem 3

# Libraries used for plotting
library(ggplot2)
library(scales)

# Allow the ability to input command line arguments and stores them in a list called 'args' as strings which can be referenced later
args <- commandArgs(trailingOnly = TRUE)
# Convert command line input to an integer to save on conversion later
orderInput <- as.integer(args[1])

# For a given input 'order' returns the the order of the taylor series for that given order
# Coefs calculates the coefficients for each element of the series
# x_grid represents the x values for the function 
# %*% multiplies the coefs by the x_grid
taylor = function(x, order) {
  coefs = (-1)^(0:order) / factorial(2 * (0:order))
  x_grid = outer(x, 2 * (0:order), "^")
  x_grid %*% coefs
}

# Normal cosine funciton, base:: represents that cos is a member of base R not a package
cosine = function(x) {
    base::cos(x)
}

# Functions subtracted from eachother to allow for an integral to be calculated
taylorCosine = function(x, order){
  coefs = (-1)^(0:order) / factorial(2 * (0:order))
  x_grid = outer(x, 2 * (0:order), "^")
  base::cos(x) - (x_grid %*% coefs)
}

# Creates a new ggplot2 plot
plot0 <- ggplot(data = data.frame(x = 0), mapping = aes(x = x)) +
    # plots the function, the args takes in the command line argument declared above when calling the function to plot the taylor series
    stat_function(fun = taylor, geom = "line", args = list(order = orderInput), mapping = aes(color = "taylor")) +
    stat_function(fun = cosine, geom = "line", linetype = "dashed", mapping = aes(color = "cosine")) +
    scale_x_continuous(limits = c(-pi/2, pi/2)) +
    # Creates the legend based on the colors declared above for the stat_functions
    scale_color_manual(name = "Functions", values = c("taylor" = "#FF0000", "cosine" = "#0000FF"), labels = c("cos(x)", paste("order", orderInput + 1,"\ntaylor approx"))) +
    # My preferred theme
    theme_bw() +
    labs(x = "x", y = "y", title = paste("Order", orderInput + 1, "Taylor Cosine Approximation")) 

# Saves the plot as a .png file named after the input
ggsave(paste0("taylorCosine",orderInput,".png"), plot = plot0, device = NULL, path = NULL,
    scale = 1, width = 20, height = 10, units = c("cm"),
    dpi = 300, limitsize = TRUE)

# Takes the integral of the different functions
# First prints the integral given by subtraction of the functions
# Then takes the percent difference of the integrals of the individual functions and prints it
cat("The integral of the cos minus the approximation is: ")
integrate(taylorCosine, lower = -pi/2, upper = pi/2, order = orderInput)
taylorInt <- integrate(taylor, lower = -pi/2, upper = pi/2, order = orderInput)
cosineInt <- integrate(cosine, lower = -pi/2, upper = pi/2)
percentDifference <- abs(((taylorInt$value - cosineInt$value)/cosineInt$value)*100)
message(paste("This gives a difference of ", percentDifference,"%"))