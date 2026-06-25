#program using classes
class bankaccountmanager:
    def __init__(self,name,starting_bal):
        self.name=name
        self.starting_bal=starting_bal
        self.history=[]
#deposit 
    def deposit(self):
        amount=float(input("enter the amount you want to add"))
        self.starting_bal+=amount
        
        self.history.append(f"amount added {amount}")
#withdraw with if statement if amount withdrwan is more then main balance
    def withdraw(self):
        amount2=float(input("enter the amount to be withdrawn"))
        if amount2>self.starting_bal:
            print("enough amount is not found")
        else:
             self.starting_bal-=amount2
             print("amount is taken")
             self.history.append(f"{amount2}")
#to check balance 
    def checkbal(self):
        print(f"the balance in account is {self.starting_bal}")
#to check tranction history
    def view_tranction_history(self):
        print(f"transaction history {self.history}")
name = input("enter account holder name:")
starting_bal = float(input("enter starting balance :"))
account = bankaccountmanager(name,starting_bal)
account.deposit()
account.withdraw()
account.checkbal()
account.view_tranction_history()

    



        
    

    


        
