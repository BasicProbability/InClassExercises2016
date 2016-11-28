class Account(object):
    '''A class representing a bank account.'''

    def __init__(self, id, pin, initial_balance = 0):
        self.balance = initial_balance
        self.id = id
        self.pin = pin

    def show_balance(self):
        '''Show the current balance of this account

        :return: The current balance
        '''
        return self.balance

    def deposit(self, amount):
        '''Deposit money in the account and return the new balance

        :param amount: The amount to be deposited
        :return: The new balance
        '''
        self.balance += amount
        return self.show_balance()

    def withdraw(self, amount, pin):
        '''Withdraw money from the account and return the new balance. If the account does not hold
        enough money to withdraw the requested amount, no money is withdrawn and a string informing the
        user that his funds are not sufficient is returned. Likewise, if the provided pin is incorrect,
        an info message is returned.

        :param amount: The amount to be withdrawn
        :param pin: The PIN of this account
        :return: The new balance or an info message
        '''
        if pin != self.pin:
            return "Wrong PIN entered"
        elif amount > self.balance:
            return "This account does not have enough funds"
        else:
            self.balance -= amount
            return self.show_balance()

    def transfer_money(self, other_account, amount, pin):
        '''Transfers money from this account to another account. If successful, the new balance of this
        account is returned. Otherwise, if funds are not sufficient or the pin is incorrect, no transaction
        takes place and an info message is returned.

        :param other_account: Another object that may or may not be an Account (check this!)
        :param amount: The amount to be transferred
        :param pin: The pin of this account
        :return: The new balance or an info message
        '''
        if not isinstance(other_account, self.__class__):
            return "The other object is not an Account"
        else:
            result = self.withdraw(amount, pin)
            if not isinstance(result, str):
                other_account.deposit(amount)
            return result

    def __eq__(self, other):
        '''Two accounts are considered equal iff their ids are equal.

        :param other: Another object
        :return: True if other is an Account and has the same id
        '''
        return isinstance(other, self.__class__) and other.id == self.id
