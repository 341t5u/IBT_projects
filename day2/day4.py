class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        self.balance -= amount
    def statement(self):
        print(f"{self.owner}: {self.balance} ETB")
almaz = Account("Almaz", 1500)
almaz.deposit(500)
almaz.withdraw(200)
almaz.statement()

class Student:
    def __init__(self,name,grade):
        self.name=name
        self.grade=grade
    def cgpa(self,mark):
        self.grade = mark
    def statement(self):
        print(f"{self.name}:{self.grade}")
samson=Student("samson","B")
samson.cgpa("A")
samson.statement()

"""class Account:
    def __init__(self, balance):
        self.__balance = balance
        @property
    def balance(self): # getter
        return self.__balance
        @balance.setter
    def balance(self, value): # setter
        if value < 0:
            raise ValueError("No negatives")
        self.__balance = value
a = Account(1500)
a.balance # 1500 (getter)
a.balance = 2000 # ok (setter)
a.balance = -5 # ValueError!"""


class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner # public
        self.__balance = balance # private
    @property
    def balance(self):
        return self.__balance
def deposit(self, amount):
    if amount <= 0:
        raise ValueError("Must be positive")
    self.__balance += amount
a = Account("Almaz", 1500)
a.deposit(500)
a.balance # 2000
a.deposit(-10) # ValueError
a.balance = -5 # AttributeError