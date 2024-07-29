a, b = map(int, input().split())

if a > 0 and int(a) == a:
    print(str(a)*3)
elif a <= 0:
    print(0)