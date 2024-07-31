a, b = map(int, input().split())
nums = [2, 4, 6, 8]
for j in nums:
    for i in range(b, a, -1):
        print(str(i) + " * " + str(j) + " = " + str(i*j), end = " / ")
    print(str(a) + " * " + str(j) + " = " + str(a*j))