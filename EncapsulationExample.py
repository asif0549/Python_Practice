class Bank():
    def __init__(self):
        self.__accn=None
        self.__name=None
        self.__balance=0

    def setAccno(self,a):
        self.__accn=a

    def setName(self,n):
        self.__name=n

    def setBalance(self,checkPass,b):
        if checkPass==123:
            self.__balance=b
        else:
            print("Invalid Password")

    def getAccno(self):
        return self.__accn
    def getName(self):
        return self.__name
    def getBalance(self):
        return self.__balance

    def DisplayDetails(self):
        print("="*20)
        print("Customer Details:\n")
        print(f"Name: {self.__name}")
        print(f"Account Number: {self.__accn}")
        print(f"Balance: {self.__balance}")

class Main:
    def main():
        b=Bank()
        accno=int(input("Enter Account Number: "))
        b.setAccno(accno)
        name=input("Enter Name: ").title()
        b.setName(name)
        balance=int(input("Enter Balance Amount: "))
        password=int(input("Enter Password: "))
        b.setBalance(password, balance)
        print(b.getAccno())
        print(b.getName())
        print(b.getBalance())
        print(b.DisplayDetails())

Main.main()
