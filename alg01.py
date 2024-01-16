# Author: Humza
# Description: This program will calculate the perpendicular slope of the slope you put in.
print("Welcome to the perpendicular slope calculator program.")
rise = int(input("Enter the rise of the original slope: "))
run = int(input("Enter the run of the slope: "))
print("Original Slope: " +str(rise) + "/" + str(run))
rise = -1 * rise
print("New Slope: "+ str(run) +"/" + str(rise))
