#by Nova James Warner
asked_once = False
print("Welcome to my calculator program! To start,")
print("select an operation you want to use:")
print('''1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Modulus
6. Special
7. Exponentiation
8. Squaring
9. Manual
''')

print("Use the manual to learn what all the operations are!")
def input_from_user():
    numbers = [""];
    numbers.insert(0,float(input("Enter the first number you want to use for the calculation:")))
    numbers.insert(1,float(input("Enter the second number you want to use for the calculation:")))
    
    return numbers
def show_manual():
    print("\nManual:")
    print("1. Addition: Add two or more values.")
    print("2. Subtraction: Subtract one value from another.")
    print("3. Multiplication: Multiply two or more values.")
    print("4. Division: Divide one value by another.")
    print("5. Modulus: Find the remainder when dividing two numbers.")
    print("6. Special: Compute (a + b) * b.")
    print("7. Exponentiation: Putting a number to a power. ")
    print("8. Squaring: Multiplying a number by 2.")
    
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
        num1 = float(input("Enter the first number you want to use for the calculation:"))
        num2 = float(input("Enter the second number you want to use for the calculation:"))
        result2 = num1 - num2
        print(num1, "-" , num2, "=", result2)
    elif choice == 3: #multiplication
        num1 = float(input("Enter the first number you want to use for the calculation:"))
        num2 = float(input("Enter the second number you want to use for the calculation:"))
        result3 = num1 * num2
        print(num1, "x" , num2, "=" ,result3)
    elif choice == 4: #division
        num1 = float(input("Enter the first number you want to use for the calculation:"))
        while True:
            num2 = float(input("Enter the second number you want to use for the calculation:"))
            if num2 == 0:
                print("You can't divide by zero")
                continue
            break
        result4 = num1 / num2
        print(num1,"/", num2, "=" ,result4)
    elif choice == 5: #modulus
        num1 = float(input("Enter the first number you want to use for the calculation:"))
        while True:
            num2 = float(input("Enter the second number you want to use for the calculation:"))
            if num2 == 0:
                print("You can't divide by zero")
                continue
            break
        result5 = num1 % num2
        print(num1,"%", num2, "=" ,result5)
    elif choice == 6:
        num1 = float(input("Enter the first number you want to use for the calculation:"))
        num2 = float(input("Enter the second number you want to use for the calculation:"))
        result6 = (num1 + num2) * num2
        print(num1,"+", num2, "x", num2, "=" ,result6)
    elif choice == 7:
        num1 = float(input("Enter the base number you want to use for the calculation:"))
        num2 = float(input("Enter the exponent you want to use for the calculation:"))
        result7 = num1 ** num2
        print(num1,"**", num2, "=" ,result7)
    elif choice == 8:
        num1 = float(input("Enter the value you want to square:"))
        result8 = num1 * 2.0
        print(num1, "**", 2.0, "=", result8)
    elif choice == 9:
        show_manual()
        continue
    if not asked_once:
        play = input("Would you like to calculate again? (y/n)").strip().lower()
        asked_once = True
        if play in ("y", "yes"):
            continue
        else:
            print("Thank you for using my calculator!")
            break