from creatures import Hobbit, ElfCook, Pupil, OrcCook, Orc, Elf

# Welcome to Middle Earth.
#
# Even though your lecturers know nothing about Middle Earth, that is what this exercise is about.
# In Middle Earth, you find different creatures such as hobbits, elves and orcs. As you all know
# hobbits love food (yes, they do) so many young hobbits go to cooking schools. But sometimes, when the
# when the wind is particularly strong, elves and orcs are blown into the Shire. Confused as they
# obviously are, or by sheer group pressure, they quickly dress up as hobbits and flee to the cooking
# schools --- the only reasonable thing to do, after all. Now the elves are loving and motivating
# creatures that ensure the pupils make quick progress, but the orcs... Oh, dear, the orcs...
# Well, you will find out all about them in this exciting new episode of Lord of the ---  yes --- Strings. Enjoy!

# In this exercise call we will play with classes, subclasses and exceptions. Your tasks are the following:
# 1) Implement the classes in creatures.py. Make sure that all required exceptions are raised.
# 2) The code below will not run because it raises lots of exceptions. Build try-except clauses where necessary to
# catch these exceptions. In the end, the code should run smoothly.
# 3) When you are finished with the three main exercises, implement the __eq__(self, other) method for each class.
# This method is implicitly called whenever you make a comparison of two object a and b of the form "a == b".
# How you define equality is up to you but please make sure that the method definitely returns false when a and b
# are not instancens of the same class.

bilbo = Hobbit("Bilbo", "blabla", 30)
bilbo = Hobbit("Biblo", "male", -30)
this is the version of bob that we would like to keep around
bilbo = Hobbit("Bilbo", "male", 30)
print("Bob's name printed correclty: {}".format(str(bilbo) == "Bilbo"))

galadriel = Elf("Galadriel")
olgot = Orc("Olgot") # Pro tip: http://fantasynamegenerators.com/lotr-orc-names.php
galadriel.cheer(bilbo)
olgot.cheer(galadriel)

# The next two lines should run without problems
galadriel.cheer(bilbo)
print("Blessing works: {}".format(bilbo.mood == "excellent"))
olgot.scare(bilbo)
print("Scaring works: {}".format(bilbo.mood == "horrible" and bilbo.age == 31))

frodo = Pupil("Frodo", -2)
# This is the version of Frodo that we would like to keep around
frodo = Pupil("Frodo")

# Define two cooks...
rosa = ElfCook("Rosa")
madoc = OrcCook("Madoc")

# Throws errors:
madoc.scare(bilbo)
rosa.cheer(bilbo)
rosa.motivate(bilbo)

madoc.scare(frodo)
print("Scaring works again: {}".format(frodo.mood == "horrible" and frodo.age == 17))
rosa.cheer(frodo)
print("Blessing works again: {}".format(frodo.mood == "excellent"))

rosa.grade(frodo, 1)
print("Bad grades work: {}".format(frodo.mood == "bad"))
rosa.grade(frodo, 6)
print("Medium grades work: {}".format(frodo.mood == "good"))
rosa.grade(frodo, 10)
print("Good grades work: {}".format(frodo.mood == "excellent"))

