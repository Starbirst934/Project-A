import math
n = 120
flag = True
while n % 2 == 0:
    n //= 2
    if flag == True:
        print(2)
        flag = False
for i in range(3, int(math.sqrt(n)) + 1, 2):
    while n % i == 0:
        print(i)
        n //= i

if n > 2:
    print(n)
