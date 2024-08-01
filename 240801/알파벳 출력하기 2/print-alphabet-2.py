n = int(input())
num = ord('A')

for i in range(n):
    print("  " * i, end = "")
    
    for j in range(n, 0, -1):
        print(chr(num), end = " ")
        #print(chr(num), end = " ")

        if num == 26:
            num = ord('A')
        else:
            num += 1

    print()
    n -= 1