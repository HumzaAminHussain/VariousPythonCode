# Author: Humza
# Description: The user enters in the slope, x coordinate, y coordinate. The program prints out the y-intercept form of the equation after processing the information.
print("Welcome to the perpendicular slope calculator program.")
rise = int(input("Enter the rise of the original slope: "))
run = int(input("Enter the run of the slope: "))
print("Original Slope: " +str(rise) + "/" + str(run))
rise = -1 * rise
print("New Slope: "+ str(run) +"/" + str(rise))
