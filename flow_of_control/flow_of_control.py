import random

#1 The following while loop is commented out because it is an infinite loop.  Fix this loop only by adding code
# and not deleting/modifying any (also, no break statements are allowed!). Then uncomment it and run it.
# You will have to terminate the run by hand if the infinite loop still occurs.

# i = 0
# while i < 100:
#     print("Hello")

#2 This week we are again given a list of twenty numbers that have been jumbled up. However, we randomly permute
# this list in a different way each time the program starts. Use for loops that brings the numbers into the correct
# order no matter what the initial permutation is. You can also write code outside the for loops if needed. The only
# thing that matters is that by the end of this exercise the numbers occur in their natural order in shuffled_list.
# You are not allowed to use trivial solutions like shuffled_list = list(range(1,21)) or shuffled_list.sort(). The
# point of this exercise is that you implement your own sorting algorithm!


shuffled_list = list(range(1,21))
random.shuffle(shuffled_list)
print(shuffled_list)

# Your code goes here!

print("The list has been ordered correctly: {}".format(shuffled_list == list(range(1,21))))

#3 Binomial MLE: the file "binomial_sample.txt" contains 100000 random draws from a binomial distribution with
# parameters n=100 and p=unknown. Write code that reads the file and computes the maximum
# likelihood estimate for p.

mle = None
n = 100
var = None

# the with statement is a more concise way to process files. It also has the advantage that the file closes
# automatically when you leave the with block. That is, you don't need to write input_file.close() in the end.
# Additional question: what's the variance of this data set assuming that the MLE is correct?
with open("binomial_sample.txt") as input_file:
    pass

print("The binomial MLE is: {}".format(mle))
print("The variance is: {}".format(var))

