class bankaccountmanager:
    def __init__(self,name,starting_bal):
        self.name=name
        self.starting_bal=starting_bal
        self.history=[]

    def deposit(self):
        amount=float(input("enter the amount you want to add"))
        self.starting_bal+=amount
        
        self.history.append(f"amount added {amount}")

    def withdraw(self):
        amount2=float(input("enter the amount to be withdrawn"))
        if amount2>self.starting_bal:
            print("enough amount is not found")
        else:
             self.starting_bal-=amount2
             print("amount is taken")
             self.history.append(f"{amount2}")

    def checkbal(self):
        print(f"the balance in account is {self.starting_bal}")

    def view_tranction_history(self):
        print(f"transaction history {self.history}")
name = input("enter account holder name:")
starting_bal = float(input("enter starting balance :"))
account = bankaccountmanager(name,starting_bal)
account.deposit()
account.withdraw()
account.checkbal()
account.view_tranction_history()

    



        
    

    


        