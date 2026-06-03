#for student marksheet
student=[1,2,3,4,5]
for student_count in student:
 m=input("print marks obtained in maths")
 s=input("print marks obtained in science")
 e=input("print marks obtained in english")
 #for finding total
total=int(m)+int(s)+int(e)
avg=total/3
if avg>=90:#grading
    grade="A"
elif avg<=89 and avg>=75:
    grade="B"
elif avg<=74 and avg>=60:
    grade="C"
elif avg<=59 and avg>=40:
    grade="D"
else:
    grade="F"
#output statements
print("===== EXAMINATION RESULT =====")
print("student 1 : {}")
print("marks obtained in maths : {}".format(m))
print("marks obtained in science : {}".format(s))
print("marks obtained in english : {}".format(e))
print("total marks obtained : {}".format(total))
print("average marks obtained : {}".format(avg))    
print("grade obtained : {}".format(grade))
print("================================")
