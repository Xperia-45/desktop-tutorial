#assigne varible
budge=int(input("enter your budget"))
age=int(input("enter your age"))
weather=str(input("preffered weather"))
#statements
if budge < 10000 and age < 18 and weather == "cold":
    print("you can go to shimla")
    print("travel with guardian is advised")
elif budge < 10000 and age >=18 and weather == "cold":
    print("you can go to shimla")
elif budge < 10000 and age < 18 and weather == "hot":
    print("you can go to goa")
    print("travel with guardian is advised")
elif budge < 10000 and age >=18 and weather == "hot":
    print("you can go to goa")
elif budge >=10000 and budge < 30000 and age < 18 and weather == "cold":
    print ("you can go to Manali")
    print("travel with guardian is advised")
elif budge >=10000 and budge < 30000 and age >=18 and weather == "cold":
    print ("you can go to manali")
elif budge >=10000 and budge < 30000 and age < 18 and weather == "hot":
    print ("you can go to pondicherry")
    print("travel with guardian is advised")
elif budge >=10000 and budge < 30000 and age >=18 and weather == "hot":
    print ("you can go to pondicherry")
elif budge >30000 and age < 18 and weather == "cold":
    print ("you can go to kashmir")
    print("travel with guardian is advised")
elif budge >30000 and age >=18 and weather == "cold":
    print ("you can go to kashmir")
elif budge >30000 and age < 18 and weather == "hot":
    print ("you can go to andaman")
    print("travel with guardian is advised")
elif budge >30000 and age >=18 and weather == "hot":
    print ("you can go to andaman")
elif budge < 10000 and age >60 and weather == "hot" and weather == "cold":
    print("you can go to shimla")
    print("you may get discount")
elif budge >=10000 and budge < 30000 and age >60 and weather == "hot" and weather == "cold":
    print ("you can go to Manali")
    print("you may get discount")
elif budge >30000 and age >60 and weather == "hot" and weather == "cold":
    print ("you can go to kashmir")
    print("you may get discount")
elif budge < 10000 and age >60 and weather == "hot":
    print("you can go to goa")
    print("you may get discount")
elif budge >=10000 and budge < 30000 and age >60 and weather == "hot":
    print ("you can go to pondicherry")
    print("you may get discount")
elif budge >30000 and age >60 and weather == "hot":
    print ("you can go to andaman")
    print("you may get discount")
    #output statements

Y=int(input("how many days you want to go ?"))
print("your total cost will be of per day "+str(budge/Y))#per day
print("have a nice trip")
print("you may leave for the trip soon ")

