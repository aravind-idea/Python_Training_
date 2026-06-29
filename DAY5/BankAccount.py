class Bankaccount:
    def __init__(self,balance,name):
        self.name=name
        self.__balance=balance

    def get__balance(self):
        return self.__balance
    def set_balance(self,amount):
        if amount>0:
            self.__balance+=amount
        else:
            print("invaild balance amount")
account=Bankaccount(500,"a")
print(account.get__balance())
account.set_balance(500)
print("total after adding",account.get__balance())
    