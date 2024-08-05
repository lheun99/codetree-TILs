a = input()
b = input()

for i in b:
    if i == "L":
        a = a[1:] + a[0]
    elif i == "R":
        a = a[-1] + a[0:-1]

print(a)