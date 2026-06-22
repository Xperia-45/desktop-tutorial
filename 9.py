import random
class Dice:
    def roll(self):
        first = random.randint(1,6)
        return first

dice = Dice()
print(dice.roll())

class Person:
    n=int(input("how many people are there?"))
    people=[]
    for i in range(n):
        name=input(f"enter name{i+1}")
        people.append(name)
    result= random.choice(people)
    print("you got:", result)

class number:
    
    def num(self):
        n=int(input("enter the numbers are there"))
        numbers=[]
        for j in range(n):
            m=input(f"enter a number{j+1}:")
            numbers.append(m)
        l= random.choice(numbers)
        print("the resulted number ", l)
n_obj=number()
n_obj.num()


    

