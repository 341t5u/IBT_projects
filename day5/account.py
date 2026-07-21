class Account:
    def __init__(self,owner,number,balance=0):
        self.owner=owner
        self.account_number=number
        self.__balance=balance 
        #make private
        self.observers = []   
    @property
    def balance(self):
        return self.__balance
    def deposit(self,amount):
        if amount <= 0:
            raise ValueError("Insufficient balance")
        self.__balance += amount 
    def subscribe(self, observer):
        self.observers.append(observer)

    def unsubscribe(self, observer):
        self.observers.remove(observer)

    def notify(self, event):
        for observer in self.observers:
            observer.update(event)

class SavingAccount(Account):
    def __init__(self, owner, number, balance=0,rate=0.05):
        super().__init__(owner, number, balance) #Calls the parent class constructor
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
        self.notify(f"{self.owner} withdrew {amount}. Balance = {self.balance}")
        
class AccountFactory:## without modifying the entire class you can extend the behavior of the class so saving or current account
    @staticmethod
    def create(kind, owner, number, balance=0):
        if kind == "savings":
            return SavingAccount(owner, number, balance)
        if kind == "current":
            return CurrentAccount(owner, number, balance)
        raise ValueError(f"Unknown type: {kind}")
    
class SMSAlert:##observer the youtube subscriber must notify when the person upload new video
    def update(self, event):
        print(f"[TeleBirr SMS] {event}")
class AuditLog:
    def update(self, event):
        print(f"[Log] {event}")
        
class BankConfig:      ##Singleton guarantees a single source of truth.(One control tower for controlling the airline)
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.interest_rate = 0.05
            cls._instance.overdraft_limit = 1000
        return cls._instance
BankConfig().interest_rate # 0.05, everywhere     
config1 = BankConfig()
config2 = BankConfig()
print(config1 is config2)   
        
        

acc = AccountFactory.create("current", "Dawit", "CBE-2")
acc.subscribe(SMSAlert())
acc.subscribe(AuditLog())
acc.withdraw(500) # both observers fire
    
    
    
"""    

# the bank opens accounts without naming classes
acc = AccountFactory.create("current", "Almaz",
"CBE-1", 16000)        
print(f"Your balance is {acc.balance}")  
acc.deposit(500)    
acc.add_interest() 
print(acc.balance)      
        

acc = Account(
"Almaz", "CBE-1001", 1500)
acc.deposit(500)
print(f"Your balance is {acc.balance}")
s = SavingAccount("Saving","Almaz", "CBE-1001", 1500)
s.deposit(500) # inherited
s.add_interest() # new
print(s.balance)
c=CurrentAccount("Almaz", "CBE-1001", 1500)
c.withdraw(700)
print(c.balance)"""