n = int(input())

num = 1
for i in range(1, n+1):
    if i % 2 == 0:
        for j in range(n):
            print(num, end = " ")
            num += 2
    else:
        for z in range(n):
            print(num, end = " ")
            num += 1
    
    if i % 2 != 0:
        num += 1
    else:
        num -= 1
    
    print()