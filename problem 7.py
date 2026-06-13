#create lists
students = []
##input statements
n = int(input("Enter number of students: "))
#for storing value
for _ in range(n):
    name = input("Enter name: ")
    s1 = int(input("Score 1: "))
    s2 = int(input("Score 2: "))
    s3 = int(input("Score 3: "))
    students.append((name, s1, s2, s3))
#for assigning topper
topper = None
top_avg = -1
#for avg and print
for name, s1, s2, s3 in students:
    avg = round((s1 + s2 + s3) / 3, 2)
    print(f"{name}: {avg:.2f}")
    if avg > top_avg:
        top_avg = avg
        topper = name
#for printing topper
print(f"Topper: {topper}")
