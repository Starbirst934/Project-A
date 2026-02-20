MAX_CANDY = int(input("Enter number of candy:"))
friend1 = 0
friend2 = 0
friend3 = 0
count = 0
for i in range(MAX_CANDY):
    if MAX_CANDY - 1 >= 0:
        MAX_CANDY = MAX_CANDY - 1 
        friend1 = friend1 + 1
        count = count + 1
    if MAX_CANDY - 4 >= 0:
        MAX_CANDY = MAX_CANDY - 4
        friend2 = friend2 + 4
        count = count + 1
    if MAX_CANDY - 9 >= 0:
        MAX_CANDY = MAX_CANDY - 9
        friend3 = friend3 + 9
        count = count + 1
print(MAX_CANDY)
print("You can give candy to")
print(count)
print("friends")