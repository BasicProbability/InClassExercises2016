import random

#1 The following function is commented out because it runs into an infinite loop. Fix this function only by adding code
# and not deleting/modifying any  (and before you ask: no break statements are allowed!). Then uncomment it and run it.
# You will have to terminate the run by hand if the infinite loop still occurs.

# def print_hello():
#     i = 0
#     while i < 100:
#         print("Hello")

#2 Recall that the factorial is of a positive integer x is defined as x! = x(x-1)!. The factorial of 0 is 0! = 1.
# Implement the fucnction factorial that takes non-negative integers as arguments. If the input is not an integer
# or negative, the function should print "Error: Invalid input <input value> to factorial()". Otherwise it should return the value
# of the factorial function for that input. Once you written the factorial function, use it to implement the
# binom_coefficient function which computes the binomial coefficient. If the second argument to that function is
# greater than the first one, the function prints "Error: second argument <value of second argument>
# value of of binom_coefficient is bigger than the first one <value of first argument>".
# Notice that by calling factorial inside binomial_coefficient you have already guarded against invalid input in the
# form of non-integers or negative numbers.

def factorial(number):
    pass
def binomial_coefficient(n,k):
    pass

random_fraction = random.random()
print("factorial gives error on fractions: {}"
      .format(factorial(random_fraction) == "Error: Invalid input {} to factorial()".format(random_fraction)))

# The check below is commented out because it will not terminate as long as factorial() has not been implemented
# random_int = -random.randint(1000)
# print("factorial gives error on negative numbers: {}"
#       .format(factorial(random_int) == "Error: Invalid input {} to factorial()".format(random_int)))

print("factorial computes correct value on 15: {}".format(factorial(15) == 1307674368000))

random_big_int = random.randint(30,50)
random_small_int = random.randint(0,30)
print("binomial_coefficient gives error when second arg is bigger: {}"
      .format(binomial_coefficient(random_small_int, random_big_int) ==
              "Error: second argument {} value of of binom_coefficient is bigger than the first one {}"
              .format(random_big_int, random_small_int)))

print("binomial_coefficient gives correct result for 8,5: {}".format(binomial_coefficient(8,5) == 56))

# 3 Binomial MLE: the file "binomial_sample.txt" contains 100000 random draws from a binomial distribution with
# parameters n=100 and p=unknown. Implement the function binomial_mle that reads the file and computes the maximum
# likelihood estimate for p.

def binomial_mle(path_to_file):
    # the with statement is a more concise way to process files. It also has the advantage that the file closes
    # automatically when you leave the with block. That is, you don't need to write input_file.close() in the end.
    with open(path_to_file) as input_file:
        pass

print("The binomial MLE is: {}".format(binomial_mle("binomial_sample.txt")))