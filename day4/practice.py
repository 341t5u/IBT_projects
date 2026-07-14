class Account:
    def __init__(self,owner,account_number,balance=0):
        self.owner=owner
        self.account_number=account_number
        self.__balance=balance
    @property
    def balance(self):
        return self.__balance
    def deposit(self,amount):
        self.__balance += amount
    def withdraw(self,amount):
        if amount > self.__balance:
            raise ValueError("Insufficient  balance")
        self.__balance -= amount
    def statement(self):
        print(f"Owner: {self.owner}")
        print(f"Account Number: {self.account_number}")
        print(f"Balance: {self.balance} Thank you for choose us")
acc=Account("Hiruy",1000189826927,260000)
acc.deposit(18430)
acc.statement()
acc.withdraw(40000)
acc.statement()
acc=Account("Selam",1000360948550,300)
acc.deposit(800)
acc.statement()
acc.withdraw(2000)
acc.statement()