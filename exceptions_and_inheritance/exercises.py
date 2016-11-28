from creatures_solution import Human, GoodLecturer, Student, EvilLecturer, Devil, Angel

# In this exercise call we will play with classes, subclasses and exceptions. Your tasks are the following:
# 1) Implement the InvalidArgumentException in errors_solution.py
# 2) Implement the classes in creatures_solution.py. Make sure that all required exceptions are raised.
# 3) The code below will not run because it raises lots of exceptions. Build try-except clauses where necessary to
# catch these exceptions. In the end, the code should run smoothly.
# 4) When you are finished with the three main exercises, implement the __eq__(self, other) method for each class.
# This method is implicitly called whenever you make a comparison of two object a and b of the form "a == b".
# How you define equality is up to you but please make sure that the method definitely returns false when a and b
# are not instancens of the same class.

bob = Human("Bob", "blabla", 30)
bob = Human("Bob", "male", -30)
# this is the version of bob that we would like to keep around
bob = Human("Bob", "male", 30)
print("Bob's name printed correclty: {}".format(str(bob) == "Bob"))

harriet = Angel("Harriet")
barry = Devil("Barry")
harriet.bless(barry)
barry.bless(harriet)

# The next two lines should run without problems
harriet.bless(bob)
print("Blessing works: {}".format(bob.mood == "excellent"))
barry.terrorise(bob)
print("Terrorising works: {}".format(bob.mood == "horrible" and bob.age == 31))

pat = Student("Pat", -2)
# This is the version of Pat that we would like to keep around
pat = Student("Pat")

heinz = GoodLecturer("Heinz")
harald = EvilLecturer("Harald")

harald.terrorise(bob)
heinz.bless(bob)
heinz.motivate(bob)

harald.terrorise(pat)
print("Terrorising works again: {}".format(pat.mood == "horrible" and pat.age == 21))
heinz.bless(pat)
print("Blessing works again: {}".format(pat.mood == "excellent"))

heinz.grade(pat, 1)
print("Bad grades work: {}".format(pat.mood == "bad"))
heinz.grade(pat, 6)
print("Medium grades work: {}".format(pat.mood == "good"))
heinz.grade((pat, 10))
print("Good grades work: {}".format(pat.mood == "excellent"))

