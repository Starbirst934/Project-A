#By Nova James Warner

print("Hi! Welcome to my trivia game.")
print("The Theme of this game is ANIMALS. Try to guess the correct answer on each question. Good luck!")

answer = input(" Question 1. What is the largest mammal on earth?")
if (answer == "blue whale"):
    print(answer + " is correct!")
    
elif (answer == "Blue Whale"):
    print(answer + " is correct!")

elif (answer == "Blue whale"):
    print(answer + " is correct!")
    
else:
    print(answer + " is incorrect!")
    
answer2 = input(" Question 2. What is the fastest bird on earth?")
if (answer2 == "peregrine falcon"):
    print(answer2 + " is correct!")
elif (answer2 == "Peregrine Falcon"):
    print(answer2 + " is correct!")
elif (answer2 == "Peregrine falcon"):
    print(answer2 + " is correct!")
    
else:
    print(answer2 + " is incorrect!")
print("Last question!")
answer3 = input("Is an arachnid an insect? Yes or no?")
if (answer3 == "no"):
    print(answer3 + " is correct!")

elif (answer3 == "No"):
    print(answer3 + " is correct!")
else:
    print(answer3 + " is incorrect!")
print("Thank you for playing!")
