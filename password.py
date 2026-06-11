#variables
correct_username = "ayush"
correct_password = "tasowe125933"
username = input('enter your username:')
password = input("enter your password: ")
#statements
if username == correct_username and password == correct_password:
    print("login successful")
elif username == correct_username and password != correct_password:
    print("incorrect password")
elif username != correct_username and password == correct_password:
    print("incorrect username")
elif username != correct_username and password != correct_password:
    print("both credential are incorrect")
    #example of username syatem 
this program can be done using lists too 
