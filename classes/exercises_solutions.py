import math
from classes.Account_solution import Account

# 1) Get all numbers whose square roots are integers (mathematical integers, not necessarily Python ints)
# from the following list. result should be assigned a list that contains the numbers and their square roots
# in tuples. That is result should be [(1,1),(4,2),....]. Only use filters and maps for this exercise!

numbers = list(range(1,10001))
result = list(map(lambda x : (x, math.sqrt(x)) ,filter(lambda x : math.sqrt(x).is_integer(), numbers)))

print("Exercise 1 seems to be correct: {}".format(len(result) == 100 and result[81] == (6724, 82.0)))

# 2) Implement the methods in the Account class.

my_account = Account(123, 1234)
your_account = Account(897, 5555, 1000)

print('Funding account works: {}'.format(my_account.deposit(100) == 100))
print('Withdrawal crashes on wrong pin: {}'.format(isinstance(my_account.withdraw(50, 1235), str)))
print('Withdrawal crashes when funds not sufficient: {}'.format(isinstance(my_account.withdraw(1000, 1234), str)))
print('Withdrawal works: {}'.format(my_account.withdraw(50,1234) == 50))

print('Equality works: {}'.format(my_account != your_account and my_account == my_account and my_account != 123))

print('Transaction crashes on wrong pin: {}'.format(isinstance(your_account.transfer_money(my_account,200,1111), str)))
print('Transaction crashes when funds not sufficient: {}'.format(isinstance(my_account.transfer_money(your_account,2000,1234), str)))
print('Transaction works: {}'.format(your_account.transfer_money(my_account,200,5555) == 800 and my_account.show_balance() == 250))
