class IndianBank:
    def __init__(self,a,n,b):
        self.accno=a
        self.name=n
        self.balance=b

    def viewDetails(self):
        print("Account Details: ")
        print("Account Num : ",self.accno)
        print("Name : ",self.name)
        print("Account Balance : ",self.balance,"\n")

    def deposit(self,amt):
        self.balance +=amt
        print(f"Amount deposited Successfully!,Updated balaced amount is {self.balance} \n")

    def withDraw(self,amt):
        if self.balance < amt:
            print("Insufficient Balance,Please Check!!!")
        else:
            self.balance -=amt
            print(f"Withdraw of {amt} is is successfully debited and current balance is {self.balance} \n")
class Main:
        @staticmethod
        def main():
            cus1=IndianBank(111,"Asif",2000)
            cus2=IndianBank(222,"Manohar",3000)
            cus3=IndianBank(333,"Dhanesh",4000)
            acno=int(input("Enter Account Number: "))
            if acno==cus1.accno:
                cus=cus1
            elif acno==cus2.accno:
                cus=cus2
            elif acno==cus3.accno:
                cus=cus3
            else:
                print("Invalid Account Number")
                return
            
            print("Select the options: \n1.Account Details \n2.deposite \n3.Withdraw \n4.Exit")
            option=int(input("Enter a valid option (1-4) only: "))
            match(option):
                case 1:cus.viewDetails()
                case 2:
                    amount=int(input("Enter amount to deposit: "))
                    cus.deposit(amount)
                case 3:
                    amount=int(input("Enter amount to withdraw: "))
                    cus.withDraw(amount)
                case 4:
                    print("Thank you!!!")
                case _:
                    print("Invalid Option!")
Main.main()

