import numpy as np
from random import sample
from timeit import Timer

#1 Below you are given two random matrices with shapes (5,3) and (5,2). Form a dot product such that
# the resulting matrix has shape (3,2).
numbers = list(range(11))

a = np.array([sample(numbers, 3) for _ in range(5)])
b = np.array([sample(numbers, 2) for _ in range(5)])
print(a)
print(b)
c = np.eye(1) # replace np.eye with your solution

print("Matrix dot product correct: {}".format(c.shape == (3,2)))


#2 Multiply the matrices c and d element-wise. This means that you should not use the dot product
# but the element in position (i,j) in d should be multiplied with the element in the same position
# in matrix e.
d = np.ones(2)*2
e = np.ones(2)*3
f = np.eye(2) # replace np.eye with your solution

print("Element-wise multiplication works: {}".format((f == np.array([[6,6],[6,6]])).all()))

#3 Using numpy instead of for-loops: Assume you are given a list of coefficients. Further assume
# that you want to use these coefficients to calculate the weighted sum for a bunch of values.
# This can be done in a for-loop as shown below. Your job is to implement the second function
# using numpy and avoiding any kind of loop. The return value of your function should again be a list
# so as to enable comparison with the first function. The reason you might want to do this is that
# matrix operations are faster than for-loops. If you are using this function often, your code
# will become more efficient. Also observe that both functions have the same docstring. Docstrings
# are supposed to give you information about what the function does, NOT about its implementation
# details.

coefficients = sample(range(100),5)
values = [sample(range(100),5) for _ in range(10)]

def weighted_sum1(coefficients, values):
    '''Compute the weighted sum of each list in a list of values. The weights are given by the coefficients.

    :param coefficients: The weights for the sums
    :param values: A list of lists of numbers
    :return: A list of sums
    '''
    result = list()

    for item in values:
        sum = 0
        for idx in range(len(item)): # idx is a commonly used abbreviation for "index"
            sum += item[idx]*coefficients[idx]
        result.append(sum)

    return result

def weighted_sum2(coefficients, values):
    '''Compute the weighted sum of each list in a list of values. The weights are given by the coefficients.

    :param coefficients: The weights for the sums
    :param values: A list of lists of numbers
    :return: A list of sums
    '''
    pass
    # TODO: implement this

print('Function implementation correct: {}'.format(weighted_sum1(coefficients, values) == weighted_sum2(coefficients, values)))

# let's check some timings, see
# https://docs.python.org/3.5/library/timeit.html for explanations
# and https://stackoverflow.com/questions/8220801/how-to-use-timeit-module

setup = '''
from random import sample
coefficients = sample(range(1000),500)
values = [sample(range(1000),500) for _ in range(200)]
from __main__ import weighted_sum1, weighted_sum2
'''

timer_obj1 = Timer("weighted_sum1(coefficients, values)", setup)
timer_obj2 = Timer("weighted_sum2(coefficients, values)", setup)
print("for-version took {} seconds".format(timer_obj1.timeit(10)))
print("np-version took {} seconds".format(timer_obj2.timeit(10)))

# experiment with these timings:
# use larger vectors and matrices
# use the repeat method to run the tests several times and only compare at the minimum times



#4 The file data.txt contains pairs of numbers. The first columns contains x-values and the second
# column contains y-values. The columns are separated by tabs. Read the file and plot the data
# points with the x values on the x-axis and the y-values on the y-axis. You will see that the result
# is far from a straight line. Find a transformation of the y-values that puts them in an almost straight
# line. Once you have achieved this, draw a line with y-intercept 0 and slope 1 across the plot. Finally,
# label the x-axis with "x" the y-axis with the name of the transformation that you have applied and give
# your plot a title. For reference, the points in your final plot and the line should look somewhat like
# in the provided pdf. The style of your plot (colour, representation of points) may very well be different.


#5 Below we have defined a main function. Make sure that this main function is executed when the
# program is run. Notice that the code above will not be run unless you include it into the main
# function.

def main():
    print("Success! You wrote your first executable script.")
