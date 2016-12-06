import numpy as np
from random import sample


#1 Below you are given two random matrices with shapes (5,3) and (5,2). Form a dot product such that
# the resulting matrix has shape (3,2).
numbers = list(range(11))

a = np.array([sample(numbers, 3) for _ in range(5)])
b = np.array([sample(numbers, 2) for _ in range(5)])
print(a)
print(b)
c = np.eye(1) # replace eye with your solution

print("Matrix dot product correct: {}".format(c.shape == (3,2)))


#2 Multiply the matrices c and d element-wise. This means that you should not use the dot product
# but the element in position (i,j) in d should be multiplied with the element in the same position
# in matrix e.
d = np.ones(2)*2
e = np.ones(2)*3
f = np.eye(2) # replace eye with your solution

print("Element-wise multiplication works: {}".format((f == np.array([[6,6],[6,6]])).all()))

#3 The file data.txt contains pairs of numbers. The first columns contains x-values and the second
# column contains y-values. The columns are separated by tabs. Read the file and plot the data
# points with the x values on the x-axis and the y-values on the y-axis. You will see that the result
# is far from a straight line. Find a transformation of the y-values that puts them in an almost straight
# line. Once you have achieved this, draw a line with intercept 0 and slope 1 across the plot. Finally,
# label the x-axis with "x" the y-axis with the name of the transformation that you have applied and give
# your plot a title. For reference, the points in your final plot and the line should look somewhat like
# in the provided png. The style of your plot (colour, representation of points) may very well be different).


#4 Below we have defined a main function. Make sure that this main function is executed when the
# program is run. Notice that the code above will not be run unless you include it into the main
# function.

def main():
    print("Success! You wrote your first executable script.")
