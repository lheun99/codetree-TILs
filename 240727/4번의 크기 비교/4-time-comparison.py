a = int(input())
bcde = map(int, input().split())

for i in bcde:
    if a > i:
        print(1)
    else:
        print(0)