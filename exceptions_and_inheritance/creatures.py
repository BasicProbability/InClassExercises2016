import random
from exceptions_and_inheritance.errors import InvalidArgumentException

class Human(object):
    '''
    Implements a humnan. Humans can have the specified genders and moods. Humans also have names and ages.
    Humans are initialised with random moods.
    '''
    moods = ["horrible", "bad", "soso", "good", "excellent"]
    genders = ["male", "female"]

    def __init__(self, name, gender = "male", age=41):
        '''Constructor

        :param name: The name of the Human
        :param gender: The gender of the Human
        :param age: The age of the Human
        :raises: InvalidArgumentException when the provided gender is not in the list of genders or
        the age is smaller than 0
        '''
        pass

    def setMood(self, mood):
        '''Set the mood of this Human.

        :param mood: The new mood of this Human
        :raises: InvalidArgumentException if the mood is not in the list of moods
        '''
        pass

    def __str__(self):
        '''Just resturn the name of the Human here.'''
        pass


class Angel(object):
    '''A devine being that help Humans by blessing them.'''

    def __init__(self, name):
        '''Constructor

        :param name: The name of this Angel
        '''
        pass

    def bless(self, human):
        '''Bless a Human. As a result, the Humans mood is excellent.

        :param human: The Human to be blessed
        :raises: TypeError if human is not a Human
        '''
        pass


class Lecturer(Human):
    '''A lecturer that gives grades to students.'''

    grades = list(range(11))

    def grade(self, student, grade):
        '''Grade a Student. If the grade is higher than 8 the student's mood becomes excellent. If the grade is
        in {6,7,8} the student's mood becomes good. The student's mood becomes bad for all lower grades.

        :param student: The Student to be graded
        :param grade: The grade to be assigned
        :raises: InvalidArgumentException if grade is not the list of grades
        :raises: TypeError if student is not a Student
        '''
        pass


class GoodLecturer(Lecturer, Angel):
    '''A creature that this a mixture of a Lecturer and an Angel. It has all the abilities of Lecturers and Angels, however,
    it can only bless Students and no other Humans. In addition, the GoodLecturer can also motivate students. This
    will cause them to study.'''

    def __init__(self, name):
        '''Constructor

        :param name: The name of this GoodLecturer
        :param age: The age of the student
        '''
        pass

    def bless(self, student):
        '''Bless a Student. As a result, the Student's mood is excellent.

        :param student: The Student to be blessed
        :raises: TypeError if student is not a Student
        '''
        pass

    def motivate(self, student):
        '''Motivate a student to study.

        :param student: The Student to be motivated
        :raises: TypeError if student is not a Student
        '''
        pass


class Student(Human):
    '''Implements a Human who visits university. Each student has an initial default intelligence of 80 and a random ability
    that is an integer in {1,2,3,4,5}'''

    def __init__(self, gender = "male", age=20, intelligence = 80):
        '''Constructor

        :param intelligence: The student's initial intelligence.
        :raises: InvalidArgumentException when the provided gender is not in the list of genders or
        the age is smaller than 0
        :raises: InvalidArgumentException if intelligence is negative
        '''
        pass

    def study(self):
        '''Let this student study. His intelligence increased by his ability when studying.'''
        pass

    def procrastinate(selfs):
        '''Let this student procrastinate. His intelligence decreased by his ability when procrastinating'''
        pass