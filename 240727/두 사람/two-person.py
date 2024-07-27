for i in range(2):
    a, b = input().split()

    if int(a) >= 19 and b == "M":
        print(1)
        break
    else:
        print(0)