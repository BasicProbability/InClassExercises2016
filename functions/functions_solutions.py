import random

#1 The following code is commented out because it runs into an infinite loop. Fix the function only by adding code
# and not deleting/modifying any (you are not allowed to use break statements). Then uncomment it and run it.
# You will have to terminate the run by hand if the infinite loop still occurs.

def print_hello(repetitions):
    '''Print "Hello" repeatedly.

    :param repetitions: The number of repetitions
    '''
    if repetitions > 0:
        print("Hello")
        print_hello(repetitions-1)

print_hello(10)

#2 Recall that the factorial of a positive integer x is defined as x! = x(x-1)!. The factorial of 0 is 0! = 1.
# Implement the function factorial that takes non-negative integers as arguments. If the input is not an integer
# or negative, the function should return "Error: Invalid input <input value> to factorial()". Otherwise it should 
# return the value of the factorial function for that input. Once you have  written the factorial function, use it to 
# implement the binom_coefficient function which computes the binomial coefficient. If the second argument to that 
# function is greater than the first one, the function return 
# "Error: second argument <value of second argument> of binom_coefficient is bigger than the first one <value of first argument>".
# Notice that by calling factorial inside binomial_coefficient you have already guarded against invalid input in the
# form of non-integers or negative numbers.

def factorial(number):
    '''The factorial of the input number.

    :param number: The input number
    :return: Factorial of number
    '''
    if number < 0 or number%1 != 0:
        return "Error: Invalid input {} to factorial()".format(number)
    elif number == 0:
        return 1
    else:
        return number*factorial(number-1)

def binomial_coefficient(n,k):
    '''The value of n choose k.

    :param n: The total set size
    :param k: The size of the subset
    :return: n choose k
    '''
    if k>n:
        return "Error: second argument {} of binom_coefficient is bigger than the first one {}".format(k,n)
    else:
        fac_n = factorial(n)
        fac_k = factorial(k)
        if isinstance(fac_n, str):
            return fac_n
        elif isinstance(fac_k, str):
            fac_k
        else:
            return fac_n/(fac_k*factorial(n-k))

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
              "Error: second argument {} of binom_coefficient is bigger than the first one {}"
              .format(random_big_int, random_small_int)))

print("binomial_coefficient gives correct result for 8,5: {}".format(binomial_coefficient(8,5) == 56))

#3 Now here comes the joy of all logicians: lambda calculus! For simple functions that are only used once
# it is often convenient to define them on the fly. Such functions do not have names and are called anonymous functions.
# Here is a simple example.
print((lambda x : x**2) (3))

# Your task is to implement and test abstract functions that do the following:
# - Return the first character of a string
# - Return the first letter of a string (that is the first non-whitespace character)
# - Check whether the number 1024 is in a list of numbers
# - Transform a number into a string
# - Takes two arguments and add them up 
# - Takes two arguments and checks whether they are of the same type

alice = " Alice"
numbers1 = list(range(1010, 1025))
numbers2 = list(range(100,200))

first_char = (lambda x : x[0] )(alice)
first_letter = (lambda x : x.strip()[0] )(alice)
number_1024_in_list = (lambda x : 1024 in x )(numbers1)
number_1024_not_in_list = (lambda x : 1024 not in x )(numbers2)
transform_number = (lambda x : str(x) )(2)
add_up = (lambda x,y : x+y )(34,23)
type_check_true = (lambda x,y : type(x) == type(y) )(123,234)
type_check_false = (lambda x,y : type(x) == type(y) )("123",234)

print("First char works: {}".format(first_char == " "))
print("First letter works: {}".format(first_letter== "A"))
print("Correct if 1024 in list: {}".format(number_1024_in_list == True)) # in the original version there was a False here which was wrong
print("Correct if 1024 not in list: {}".format(number_1024_not_in_list == True)) # in the original version there was a False here which was wrong
print("Number transformation works: {}".format(transform_number == "2"))
print("Addition works: {}".format(add_up == 57))
print("Type check if types match works: {}".format(type_check_true == True))
print("Type check if types don't match works: {}".format(type_check_false == False))
