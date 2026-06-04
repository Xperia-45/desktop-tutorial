students=[1,2]
for student in students:
  m=int(input("enter marks obtained in maths: "))
  s=int(input("enter marks obtained in science: "))
  e=int(input("enter marks obtsined in english: "))
  total=int(m)+int(s)+int(e)
  avg=total/3
  if avg>=90:
    grade="A"
  elif avg<=89 and avg>=75:
    grade="B"
  elif avg<=74 and avg>=60:
    grade="C"
  elif avg<=59 and avg>=40:
    grade="D"
  else:
    grade="F"
    print("=======EXAMINATION RESULT========")
    print("STUDENT NUMBER: ",student)
    print("marks obtained in maths: ",m)
    print("marks obtained in science: ",s)
    print("marks obtained in english: ",e)
    print("total marks obtained: ",total)
    print("average marks obtained: ",avg)
    print("grade obtained: ",grade)
    print("=================================")
averages=[]
averages.append(avg)
print(max(averages))
print(min(averages))

