MAX_CANDY = int(input("Enter amount of candy:"))
count = 0

for i in range(MAX_CANDY):
    count = count + 1
    if count > 0:
        print('Friend {} gets {} pieces of candy'.format(count, count ** 2))
        MAX_CANDY = MAX_CANDY - (count ** 2)

    if MAX_CANDY <= 0:
        print('We are out of candy!')
        break

print('You can give candy to {} friend(s)'.format(count))
