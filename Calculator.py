#by Nova James Warner
previous = None
asked_once = False
history = []
print("Welcome to my calculator program! To start,")
print("select an operation you want to use:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Modulus")
print("6. Special")
print("7. Exponentiation")
print("8. Squaring")
print("9. Previous")
print("10. Calculate 3 numbers")
print("11. Calculation history")
print("12. Exit")
print("13. Manual")
print("Use the manual to learn what all the operations and functions do!")
def input_from_user():
    number = []
    while True:
        try:
            number.insert(0, float(input("Enter the first number you want to use for the calculation: ")))
            number.insert(1, float(input("Enter the second number you want to use for the calculation: ")))
            return number
        except(ValueError,SyntaxError,RuntimeError,TypeError):
            print("Please enter valid numbers like 3 or 4.5.")

def compute3():
    try:
        choice3 = int(input("Enter what operation you want to use from 1-3:"))
    except(ValueError, SyntaxError, RuntimeError, TypeError):
        print("Please enter an operation from 1-3.")
    
    num1 = float(input("Enter the first number you want to use for the calculation:"))
    num2 = float(input("Enter the second number you want to use for your calculation:"))
    num3 = float(input("Enter the third number you want to use for your calculation:"))

    if choice3 == 1:
        result = num1 + num2 + num3
        history.append(f"{num1} + {num2} + {num3} = {result}")
        print(num1, "+", num2, "+", num3, "=", result)

    elif choice3 == 2:
        result = num1 - num2 - num3
        history.append(f"{num1} - {num2} - {num3} = {result}")
        print(num1, "-", num2, "-", num3, "=", result)
    
    elif choice3 == 3:
        result = num1 * num2 * num3
        history.append(f"{num1} x {num2} x {num3} = {result}")
        print(num1, "x", num2, "x", num3, "=", result)

def show_history():
    if not history:
        print("You have no previous calculations.")
    else:
        for i, line in enumerate(history, 1):
            print(f"{i}: {line}")

def show_manual():
    print("\nManual:")
    print("1. Addition: Add two or more values.")
    print("2. Subtraction: Subtract one value from another.")
    print("3. Multiplication: Multiply two or more values.")
    print("4. Division: Divide one value by another.")
    print("5. Modulus: Find the remainder when dividing two numbers.")
    print("6. Special: Compute (a + b) * b.")
    print("7. Exponentiation: Putting a number to a power. ")
    print("8. Squaring: Multiply a number by itself.")
    print("9. Previous: Use your previous answer in another calculation.")
    print("10. Calculate 3 numbers: Add, subtract, or multiply 3 numbers at a time.")
    print("11. Calculation history: Shows all, if any, of your previous calculations.")
    print("12. Exit: Closes the program.")
    print("13. Manual: Shows the descriptions of all the functions and operations including this one.")
while True:
    try:
        choice = int(input("\nEnter the number of your choice of operation or exit using '12'.(1 = addition, 2 = subtraction, etc.): ").strip())
    except(ValueError):
        print("Please enter a whole number from 1-13.")
        continue

    if choice < 1:
        print("Please enter a whole number from 1-13.")
        continue

    if choice > 13:
        print("Please enter a whole number from 1-13.")
        continue

    if choice == 1:#addition

        #num1 = int(input("Enter the first number you want to use for the calculation:"))
        #num2 = int(input("Enter the second number you want to use for the calculation:"))
        #result1 = num1 + num2
        #print(num1, "+", num2, "=", result1)

        numbers = input_from_user()
        result = numbers[0] + numbers[1]
        history.append(f"{numbers[0]} + {numbers[1]} = {result}")
        print(numbers[0], "+", numbers[1], "=", result)
        previous = result

    elif choice == 2:#subtraction

        num1 = float((input("Enter the first number you want to use for the calculation:")).strip())
        num2 = float((input("Enter the second number you want to use for the calculation:")).strip())
        result = num1 - num2
        history.append(f"{num1} - {num2} = {result}")
        print(num1, "-" , num2, "=", result)
        previous = result
    elif choice == 3: #multiplication

        num1 = float((input("Enter the first number you want to use for the calculation:")).strip())
        num2 = float((input("Enter the second number you want to use for the calculation:")).strip())
        result = num1 * num2
        history.append(f"{num1} * {num2} = {result}")
        print(num1, "x" , num2, "=" ,result)
        previous = result
    elif choice == 4: #division

        num1 = float((input("Enter the first number you want to use for the calculation:")).strip())
        while True:
            num2 = float((input("Enter the second number you want to use for the calculation:")).strip())
            if num2 == 0:
                print("You can't divide by zero.")
                continue
            break
        result = num1 / num2
        history.append(f"{num1} / {num2} = {result}")
        print(num1,"/", num2, "=" ,result)
        previous = result
    elif choice == 5: #modulus

        num1 = float((input("Enter the first number you want to use for the calculation:")).strip())
        while True:
            num2 = float((input("Enter the second number you want to use for the calculation:")).strip())
            if num2 == 0:
                print("You can't divide by zero.")
                continue
            break
        result = num1 % num2
        history.append(f"{num1} % {num2} = {result}")
        print(num1,"%", num2, "=" ,result)
        previous = result
    elif choice == 6: #special  operation

        num1 = float((input("Enter the first number you want to use for the calculation:")).strip())
        num2 = float((input("Enter the second number you want to use for the calculation:")).strip())
        result = (num1 + num2) * num2
        history.append(f"{num1} + {num2} x {num2} = {result}")
        print(num1,"+", num2, "x", num2, "=" ,result)
        previous = result
    elif choice == 7: #Exponentiation

        num1 = float((input("Enter the base number you want to use for the calculation:")).strip())
        num2 = float((input("Enter the exponent you want to use for the calculation:")).strip())
        result = num1 ** num2
        history.append(f"{num1} ** {num2} = {result}")
        print(num1,"**", num2, "=" ,result)
        previous = result
    elif choice == 8: #squaring

        num1 = float((input("Enter the value you want to square:")).strip())
        result = num1 ** 2.0
        history.append(f"{num1} ** 2.0 = {result}")
        print(num1, "**", 2.0, "=", result)
        previous =  result

    elif choice == 9: #previous
        choice2 = 0
        if previous is not None:
            num1 = previous
            while True:
                try:
                    choice2 = int((input("Enter the operation you would like to use with your previous answer:")).strip())
                except(ValueError, TypeError, SyntaxError, RuntimeError):
                    print("Please enter a valid operation from 1-8.")

                if choice2 < 1:
                    print(" Please enter a valid operation from 1-8.")
                    continue

                if choice2 > 8:
                    print(" Please enter a valid operation from 1-8.")
                    continue
                else:
                    break


            if choice2 == 1:
                num2 = float((input("Enter the second number you want to use for your calculation:")).strip())
                result = num1 + num2
                print(num1, "+", num2, "=", result)
                previous = result
                history.append(f"{num1} + {num2} = {result}")

            elif choice2 == 2:
                num2 = float((input("Enter the second number you want to use for your calculation:")).strip())
                result = num1 - num2
                print(num1, "-", num2, "=", result)
                previous = result
                history.append(f"{num1} - {num2} = {result}")

            elif choice2 == 3:
                num2 = float((input("Enter the second number you want to use for your calculation:")).strip())
                result = num1 * num2
                print(num1, "x", num2, "=", result)
                previous = result
                history.append(f"{num1} x {num2} = {result}")

            elif choice2 == 4:
                while True:
                    num2 = float((input("Enter the second number you want to use for the calculation:")).strip())
                    if num2 == 0:
                        print("You can't divide by zero.")
                        continue
                    break
                result = num1 / num2
                print(num1, "/", num2, "=", result)
                previous = result
                history.append(f"{num1} / {num2} = {result}")

            elif choice2 == 5:
                while True:
                    num2 = float((input("Enter the second number you want to use for the calculation:")).strip())
                    if num2 == 0:
                        print("You can't divide by zero.")
                        continue
                    break
                result = num1 % num2
                print(num1, "%", num2, "=", result)
                previous = result
                history.append(f"{num1} % {num2} = {result}")

            elif choice2 == 6:
                num2 = float((input("Enter the second number you want to use for the calculation:")).strip())
                result = (num1 + num2) * num2
                history.append(f"{num1} + {num2} x {num2} = {result}")
                print(num1,"+", num2, "x", num2, "=" ,result)
                previous = result

            elif choice2 == 7:
                num2 = float((input("Enter the exponent you want to use for the calculation:")).strip())
                result = num1 ** num2
                history.append(f"{num1} ** {num2} = {result}")
                print(num1,"**", num2, "=" ,result)
                previous = result

            elif choice2 == 8:
                result = num1 ** 2.0
                history.append(f"{num1} ** 2.0 = {result}")
                print(num1, "**", 2.0, "=", result)
                previous =  result
        else:
            print("You have no previous calculation to work with!")
            continue

    elif choice == 10: #3 number calculation
        compute3()
        continue

    elif choice == 11: #Calculation history
        print("Here are your previous calculation(s):")
        show_history()
        continue

    elif choice == 12: #exit
        print("Thank you for using my calculator!")
        break

    elif choice == 13: #manual
        show_manual()
        continue

    if not asked_once:
        play = input("Would you like to use the calculator again? (y/n)").strip().lower()
        asked_once = True
        if play in ("y", "yes"):
            continue

        else:
            print("Thank you for using my calculator!")
            break
