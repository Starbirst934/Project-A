#By Nova James Warner
count = 0
playing = True
while playing:
    print("Hi! Welcome to my trivia game.")
    print("The Theme of this game is ANIMALS. Try to guess the correct answer on each question. Good luck!")

    answer = input(" Question 1. What is the largest mammal on earth?")
    if (answer == "blue whale"):
        print(answer + " is correct!")
        count = count + 1
    elif (answer == "Blue Whale"):
        print(answer + " is correct!")
        count = count + 1
    elif (answer == "Blue whale"):
        print(answer + " is correct!")
        count = count + 1
    else:
        print(answer + " is incorrect!")
    
    answer2 = input(" Question 2. What is the fastest bird on earth?")
    if (answer2 == "peregrine falcon"):       
        print(answer2 + " is correct!")
        count = count + 1
    elif (answer2 == "Peregrine Falcon"):
        print(answer2 + " is correct!")
        count = count + 1
    elif (answer2 == "Peregrine falcon"):
        print(answer2 + " is correct!")   
        count = count + 1 
    else:
        print(answer2 + " is incorrect!")
    print("Last question!")
    answer3 =input("Is an arachnid an insect? Yes or no?")
    if (answer3 == "no"):
        print(answer3 + " is correct!")
        count = count + 1
    elif (answer3 == "No"):
        print(answer3 + " is correct!")
        count = count + 1
    else:
        print(answer3 + " is incorrect!")
    if count == 1:
        print("You got 1 out of 3 questions correct! Better luck next time!")
    elif count == 2:
        print("You got 2 out of 3 questions correct! So close!")
    elif count == 3:
        print("You got 3 out of 3 questions correct! Good job!")
    elif count == 0:
        print("You got 0 out of 3 questions correct! That's ok!")
    game = input("Would you like to play again? Yes or no.")
    if game == "Yes":
        continue
    elif game == "yes":
        continue
    elif game == "y":
        continue
    elif game == "YES":
        continue
    if game == "No":
        print("Thank you for playing!")
        break
    elif game == "no":
        print("Thank you for playing!")
        break
    elif game == "n":
        print("Thank you for playing!")
        break
    elif game == "NO":
        print("Thank you for playing!")
        break
    else:
        print("Invalid input.")
        break
