a = int(input())
i = 1
while a % i <= 1:
    a //= i 
    i += 1
    print(i)