n = int(input())

for i in range(n, 0, -1):
    a = n - i

    print("*" * i, end = "")
    print(" " * a, end = "")
    print(" " * a, end = "")
    print("*" * i)