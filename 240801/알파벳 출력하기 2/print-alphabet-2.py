n = int(input())
num = ord('A')

for i in range(n):
    print("  " * i, end = "")
    
    for j in range(n, 0, -1):
        print(chr(num), end = " ")
        #print(chr(num), end = " ")
        num += 1
    n -= 1
    print()