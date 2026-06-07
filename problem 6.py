#for input of information
n=str(input("Enter the name of contacts you want to add: "))
my_list1= []
for i in range(n):
    item = input(f"Enter the name {i+1}: ")
    my_list1.append(item)
#for taking input
phone_number = int(input("enter the phone number: "))
my_list2= []
for i in range(n):
    item = input(f"enter the phone number {i+1}: ")
    my_list2.append(item)
#for taking input email
email = (input("enter the email: "))
my_list3= []
for i in range(n):
    item = input(f"enter the email {i+1}: ")
    my_list3.append(item)
print("=====CONTACTS=====")#for menu
for i in range(n):
    print(f"Name: {my_list1[i]}")
    print(f"Phone Number: {my_list2[i]}")
    print(f"Email: {my_list3[i]}")
    print("===================")
    search_name = input("enter the name to search (or 'exit' to quit): ")
    found = True
    print("=====SEARCH RESULTS=====")
    for i in range(n):
        if search_name == my_list1[i]:
            print(f"Name: {my_list1[i]}")
            print(f"Phone Number: {my_list2[i]}")
            print(f"Email: {my_list3[i]}")
            print("===================")
            found = True
    if not found:
        print("Contact not found.")

while True:#for repeating menu

    print("=====MENU=====")
    print("do you want to update the contact? (yes/no)")
    choice = input("enter your choice:")
    if choice.lower()=="yes":
        update_name = input("enter the name to update: ")
        found = True
        for i in range(n):
            if update_name == my_list1[i]:
                new_phone_number = input("enter the new phone number: ")
                my_list2[i] = new_phone_number
                new_email = input("enter the new email: ")
                my_list3[i] = new_email
                print("Contact updated successfully.")
                found = False
                break
        if not found:
            print("Contact not found.")

print("do you want to delete the contact? (yes/no)")#for deleting
choice2  = input("enter your choice:")
if choice2.lower()=="yes":
    delete_name = input("enter the name to delete: ")
    found = True
    for i in range(n):
        if delete_name == my_list1[i]:
            del my_list1[i]
            del my_list2[i]
            del my_list3[i]
            print("Contact deleted successfully.")
            found = False
            break
    if not found:
        print("Contact not found.")



