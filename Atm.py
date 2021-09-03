class atm(object):
    def __init__(self, card,pin,balance):
        self.card = card
        self.pin = pin
        self.balance=balance

    def checkAtm(self):
        if(len(self.card)!=16):
            print("Please check your ATM card no.\n There should be 16 digits.")
        if(len(self.pin)<4):
            print("Please check your PIN")
    
    def balanceP(self):
        return(self.balance)
    
    def balanceW(self,amtW):
        withdrawl=self.balance-amtW
        print("Your balace is now:", withdrawl)
        self.balance=withdrawl
    
    def balanceA(self,amtA):
        add=self.balance+amtA
        print("Your balace is now:", add)
        self.balance=add


atmcard=(input("Please enter your ATM card no.: "))
pin=(input("Please enter your PIN: "))
person1=atm(atmcard,pin,50000)
print(person1.checkAtm())
print(person1.balanceP())

w=int(input('Please enter the amount you want to withdraw: '))
print(person1.balanceW(w))

a=int(input('Please enter the amount you want to add: '))
print(person1.balanceA(a))