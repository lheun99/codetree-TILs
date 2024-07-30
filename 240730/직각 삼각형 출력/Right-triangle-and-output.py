n = int(input())
a = 1
for i in range(n):
    if n % 2 == 0:
        i *= 2
        print("*" * i)
    else:
        i = i * 2 + 1
        print("*" * i)