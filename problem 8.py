#input for roll numnber
print("this program converts digits to string")
number = input("enter your roll number")
#dictionerys created
number_mapping ={
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine",
    "0": "zero",
}
#for adding space
output=""
#for loop for printing 
for r in number:
    output += number_mapping.get(r,"!")+"  "#to get value from dictioners
output = output.strip() + "!"
print(output)
