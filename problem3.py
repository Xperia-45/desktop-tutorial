#variables
max_number_guess = 3
guess_count = 0
number= 7
#output
print("welcome to the single digit number guessing game ")
print("you have max three chances to guess the number")
#while clause
while max_number_guess > guess_count:
    print("guess the number")
    guess = int(input())
    guess_count += 1
    if guess == number:
        print("congratulations you guessed the number in " + str(guess_count) + " guesses")
        break
    elif guess < number:
        print("your guess is too low")
    elif guess > number:
        print("your guess is too high")
        if guess_count == max_number_guess:
            print("sorry you have used all your chances the number was " + str(number))
            print("-----------------GAME ENDS HERE -------------------")
          print("game ends here you may restart if you wish ")
            
















