import random
Game = True
human_choice = ''
computer_choice = ''
computer_score = 0
human_score = 0
number_of_ties = 0
while Game == True:    
    if human_choice or computer_choice == '':
        human_choice = input("Enter rock, paper, or scissors")
        computer_choice = random.choice(['rock','paper','scissors'])
    if human_choice == 'rock' and computer_choice == 'scissors':
        print("You win!")
        human_score += 1
    elif human_choice == 'scissors' and computer_choice == 'rock':
        print("Computer wins!")
        computer_score += 1
    elif human_choice == 'paper' and computer_choice == 'rock':
        print("You win!")
        human_score += 1
    elif human_choice == 'rock' and computer_choice == 'paper':
        print("Computer wins!")
        computer_score += 1
    elif human_choice == 'scissors' and computer_choice == 'paper':
        print("You win!")
        human_score += 1
    elif human_choice == 'paper' and computer_choice == 'scissors':
        print("Computer wins!")
        computer_score += 1
    elif human_choice == computer_choice:
        print("It's a tie!")
        number_of_ties += 1
    else:
        print("Invalid input")
        continue
        Game = True
        
    print('human chose ' + human_choice)
    print('the computer chose ' + computer_choice)
    answer = input("Would you like to keep playing? YES or NO.")
    if answer == 'YES':
        continue
    elif answer == 'yes':
        continue
    elif answer == 'y':
        continue
    elif answer == 'NO':
        print("You won...")
        print(human_score)
        print("time(s)!")
        print("The computer won...")
        print(computer_score)
        print("time(s)!")
        if computer_score > human_score:
            print("the computer says, 'Good game!'")
            print("Thank you for playing!")
            break
        elif computer_score == human_score:
            print("It was a tie!")
            print("Thank you for playing!")
            break
        elif computer_score < human_score:
            print("You won the game! Congratulations!!!")
            print("Thank you for playing!")
        break
    elif answer == 'no':
        print("You won...")
        print(human_score)
        print("time(s)!")
        print("The computer won...")
        print(computer_score)
        print("time(s)!")
        if computer_score > human_score:
            print("the computer says, 'Good game!'")
            print("Thank you for playing!")
            break
        elif computer_score == human_score:
            print("It was a tie!")
            print("Thank you for playing!")
            break
        elif computer_score < human_score:
            print("You won the game! Congratulations!!!")
            print("Thank you for playing!")
        break
    elif answer == 'n':
        print("You won...")
        print(human_score)
        print("time(s)!")
        print("The computer won...")
        print(computer_score)
        print("time(s)!")
        if computer_score > human_score:
            print("the computer says, 'Good game!'")
            print("Thank you for playing!")
            break
        elif computer_score == human_score:
            print("It was a tie!")
            print("Thank you for playing!")
            break
        elif computer_score < human_score:
            print("You won the game! Congratulations!!!")
            print("Thank you for playing!")
        break
    else:
        print("Invalid input")
        Game == True