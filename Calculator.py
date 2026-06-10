#by Nova James Warner
print("Welcome to my calculator program! To start,")
print("select an operation you want to use:")
print('''1. Addition
2. Subtraction
3. Multiplication
4. Division
5. modulus
6. special
''')

print('''The special operation adds two chosen numbers together and then multiplies the
answer from the addition by the second chosen number.''')

def input_from_user():
    numbers = [""];
    numbers.insert(0,int(input("Enter the first number you want to use for the calculation:")))
    numbers.insert(1,int(input("Enter the second number you want to use for the calculation:")))
    
    return numbers

    

    
while True:
    choice = int(input('''

Enter the number of your choice of operation (1 = addition, 2 = subtraction, etc.):'''))
    
    if choice == 1:#addition

        #num1 = int(input("Enter the first number you want to use for the calculation:"))
        #num2 = int(input("Enter the second number you want to use for the calculation:"))
        #result1 = num1 + num2
        #print(num1, "+", num2, "=", result1)
         
        numbers = input_from_user()
        result1 = numbers[0] + numbers[1]
        print(numbers[0], "+", numbers[1], "=", result1)
        
    elif choice == 2:#subtraction
        num1 = int(input("Enter the first number you want to use for the calculation:"))
        num2 = int(input("Enter the second number you want to use for the calculation:"))
        result2 = num1 - num2
        print(num1, "-" , num2, "=", result2)
    elif choice == 3: #multiplication
        num1 = int(input("Enter the first number you want to use for the calculation:"))
        num2 = int(input("Enter the second number you want to use for the calculation:"))
        result3 = num1 * num2
        print(num1, "x" , num2, "=" ,result3)
    elif choice == 4: #division
        num1 = int(input("Enter the first number you want to use for the calculation:"))
        num2 = int(input("Enter the second number you want to use for the calculation:"))
        result4 = num1 / num2
        print(num1,"/", num2, "=" ,result4)
    elif choice == 5: #modulus
        num1 = int(input("Enter the first number you want to use for the calculation:"))
        num2 = int(input("Enter the second number you want to use for the calculation:"))
        result5 = num1 // num2
        print(num1,"//", num2, "=" ,result5)
    elif choice == 6:
        num1 = int(input("Enter the first number you want to use for the calculation:"))
        num2 = int(input("Enter the second number you want to use for the calculation:"))
        result6 = (num1 + num2) * num2
        print(num1,"+", num2, "x", num2, "=" ,result6)
    play = input("Would you like to calculate again? (y/n)")
    if play == "y":
        continue
    elif play == "n":
        break
    else:
        print(play,"is not a valid option")
        break