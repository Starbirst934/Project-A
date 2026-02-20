for i in range(1,101,1):
    print(i)
    if i % 3 == 0:
        print("fizz")
    if i % 5 and 3 == 0:
        print("fizzbuzz")
    elif i % 5 == 0:
        print("buzz")