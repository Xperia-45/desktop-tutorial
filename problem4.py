#car game
while True:# if ture this block will execute 
    commmand = input("enter a command (start/stop/quit): ")
    if commmand == "start":
     print('car has started')
    command = input("enter  a command (start/stop/quit): ")
    if command == "stop":
        print("car has stopped")
    elif command == "quit":
        print("quiting the game")
        break #to remove the loop form rerunning
    else:#if user enters invalid command
        print("invalid command")
        print("you can restart the game as you  wish")
        
