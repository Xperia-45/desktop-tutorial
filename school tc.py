sch= input("enter school name  ")
name=input("enter the name of student   ")
father=input("enter the name of father  ")
roll_number=input("enter the roll number   ")
standerd=input("enter the class of student along with section    "   )
conduct=input("enter the behaviour grade of student in the session A TO D   " )
conduct=conduct.upper()
roll_mapping={
    "1":"one",
    "2":"two",
    "3":"three",
    "4":"four",
    "5":"five",
    "6":"six",
    "7":"seven",
    "8":"eight",
    "9":"nine",
    "0":"zero"
}
uppercase=sch.upper()
roll=""
for ch in roll_number:
    roll+=roll_mapping.get(ch) + " "
roll= roll.strip()
print(f"----------------{sch}----------------")
print("       TRANSFER CERTIFICATE        ")
print(" thanks for this heart full journey with us ")
print(f"the student of class {standerd} has passed {standerd} ")
print(f"The name of student {name}son of {father} with roll number    {roll}")
if conduct=="A":
    print("student has great performance through out the year")
elif conduct=="B":
    print("the students performance is good through out the year")
elif conduct=="C":
    print("the student has average performance through out the year ")
elif conduct=="D":
    print("the student has bad performance through out the year")
print("BEST HOPES FOR YOUR FUTURE")
print("------next journey starts soon------")


