print("this program converts digits to string")
number = input("enter your roll number")
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
output=""
for r in number:
    output += number_mapping.get(r,"!")+"  "
output = output.strip() + "!"
print(output)