#shopping discount 
bill=input("enterr the bill amount")
member=input("arre you member of the store (yes/no)?")
discount=""
#statements
if member=="yes" and int(bill)>5000:
    print("you get 20% discount")
    discount=20
elif member=="no" and int(bill)>5000:
    print("you get 10% discount")
    discount=10
elif member=="yes" and int(bill)<5000 and int(bill)>2000:
    print("you get 10% discount")
    discount=10
elif member=="no" and int(bill)<5000 and int(bill)>2000:
    print("you get 5% discount")
    discount=5
else:
    int(bill)<2000
    print("you get no discount")
    discount=0
    #calculaations
discount_amount=int(bill)*int(discount)/100
amount_to_pay=int(bill)-discount_amount
#output statements
print("discount amount" + str(discount_amount))
print("total amount to pay" + str(amount_to_pay))
#it can be done using  lists too
    
