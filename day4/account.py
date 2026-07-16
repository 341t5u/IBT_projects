class Account:
    def __init__(self,owner,number,balance=0):
        self.owner=owner
        self.account_number=number
        self.__balance=balance
    @property
    def balance(self):
        return self.__balance
    def deposit(self,amount):
        if amount <= 0:
            raise ValueError("Insufficient balance")
        self.__balance += amount
class SavingAccount(Account):
    def __init__(self, owner, number, balance=0,rate=0.05):
        super().__init__(owner, number, balance)
        self.rate= rate
    def add_interest(self):
        self.deposit(self.balance*self.rate)
class CurrentAccount(Account):
    def __init__(self, owner, number, balance=0,od=1000):
        super().__init__(owner, number, balance)
        self.overdraft=od
    def withdraw(self,amount):
        if amount>self.balance + self.overdraft:
            raise ValueError("Over limit")
        self._Account__balance -= amount 
acc = Account(
"Almaz", "CBE-1001", 1500)
acc.deposit(500)
print(f"Your balance is {acc.balance}")
s = SavingAccount(
"Almaz", "CBE-1001", 1500)
s.deposit(500) # inherited
s.add_interest() # new
print(s.balance)
c=CurrentAccount("Almaz", "CBE-1001", 1500)
c.withdraw(700)
print(c.balance)