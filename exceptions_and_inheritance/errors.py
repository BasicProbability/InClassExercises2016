class InvalidArgumentException(Exception):
    '''An Exception that should be raised whenever an invalid argument for a function or method is provided.
    Note: In Python one would usually use the built-in ValueError in that case. We are designing our own Exception
    here solely for exercise purposes.'''

    def __init__(self, argument, value):
        '''Constructor

        :param argument: The name of the argument for which the invalid value was provided
        :param value: The invalid value
        '''

        # An error message that explains the user what went wrong
        self.message = "{} is not valid for argument {}".format(value, argument)

    def __str__(self):
        '''Return the error message here'''
        return self.message
