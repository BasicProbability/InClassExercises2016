import random
from exceptions_and_inheritance.errors import InvalidArgumentException

class Hobbit(object):
    '''
    Implements a hobbit. Hobbits can have the specified genders and moods. Hobbits also have names and ages.
    Hobbits are initialised with random moods.
    '''
    moods = ["horrible", "bad", "soso", "good", "excellent"]
    genders = ["male", "female"]

    def __init__(self, name, gender = "male", age=41):
        '''Constructor

        :param name: The name of the Hobbit
        :param gender: The gender of the Hobbit
        :param age: The age of the Hobbit
        :raises: InvalidArgumentException when the provided gender is not in the list of genders or
        the age is smaller than 0
        '''
        pass

    def setMood(self, mood):
        '''Set the mood of this Hobbit.

        :param mood: The new mood of this Hobbit
        :raises: InvalidArgumentException if the mood is not in the list of moods
        '''
        pass

    def __str__(self):
        '''Just resturn the name of the Hobbit here.'''
        pass

class Elf(object):
    '''A devine being that help Hobbits by cheering them.'''

    def __init__(self, name):
        '''Constructor

        :param name: The name of this Elf
        '''
        pass

    def cheer(self, hobbit):
        '''Cheer a Hobbit. As a result, the Hobbits mood is excellent.

        :param hobbit: The Hobbit to be cheered
        :raises: TypeError if hobbit is not a Hobbit
        '''
        pass

class Orc(object):
    '''An orc that typically only scares Hobbits.'''

    def __init__(self, name):
        '''Constructor

        :param name: The name of this Orc
        '''
        pass

    def scare(self, hobbit):
        '''Scare a Hobbit. Her mood will be horrible as a result and she will age by one year.

        :param hobbit: The Hobbit to be scared
        :raises: TypeError if hobbit is not a Hobbit
        '''
        pass

class Cook(Hobbit):
    '''A cook who trains new cooks (and apparently does not cook herself)'''

    grades = list(range(11))

    def grade(self, pupil, grade):
        '''Grade a Pupil. If the grade is higher than 8 the pupil's mood becomes excellent. If the grade is
        in {6,7,8} the pupil's mood becomes good. The pupil's mood becomes bad for all lower grades.

        :param pupil: The Pupil to be graded
        :param grade: The grade to be assigned
        :raises: InvalidArgumentException if grade is not the list of grades
        :raises: TypeError if pupil is not a Pupil
        '''
        pass

class OrcCook(Cook, Orc):
    '''A creature that is a mixture of a Cook and a Orc. It has all the abilities of Cooks and Orcs, however,
    for some completely unknown reason it can only scare Pupils and no other Hobbits.
    '''

    def __init__(self, name):
        '''Constructor

        :param name: The name of this OrcCook
        '''
        pass

    def scare(self, pupil):
        '''Scare a Pupil. Her mood will be horrible as a result and she will age by one year.

        :param pupil: The Pupil to be scared
        :raises: TypeError if pupil is not a Pupil
        '''
        pass

class ElfCook(Cook, Elf):
    '''A creature that this a mixture of a Cook and an Elf. It has all the abilities of Cooks and Elfs, however,
    it can only cheer Pupils and no other Hobbits. In addition, the ElfCooks can also motivate pupils. This
    will cause them to cook.'''

    def __init__(self, name):
        '''Constructor

        :param name: The name of this ElfCook
        :param age: The age of the pupil
        '''
        pass

    def cheer(self, pupil):
        '''Cheer a Pupil. As a result, the Pupil's mood is excellent.

        :param pupil: The Pupil to be cheered
        :raises: TypeError if pupil is not a Pupil
        '''
        pass

    def motivate(self, pupil):
        '''Motivate a pupil to cook.

        :param pupil: The Pupil to be motivated
        :raises: TypeError if pupil is not a Pupil
        '''
        pass

class Pupil(Hobbit):
    '''Implements a Hobbit visiting cooking school.
    When cooking, the productivity of the pupil increases on a scale of 1 to 100.
    Each pupil has an initial default productivity of 5 and a random ability that
    is an integer in {1,2,3,4,5}'''

    def __init__(self, gender = "female", age=16, productivity = 5):
        '''Constructor

        :param productivity: The pupil's initial productivity.
        :raises: InvalidArgumentException when the provided gender is not in the list of genders or
        the age is smaller than 0
        :raises: InvalidArgumentException if productivity is negative
        '''
        pass

    def cook(self):
        '''Let this pupil cook. Her productivity increased by her ability when cooking.'''
        pass
