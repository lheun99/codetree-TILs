a = input()
b = input()

n1 = ""
for i in a:
    if i.isdigit():
        n1 += i

n2 = ""
for i in b:
    if i.isdigit():
        n2 += i

print(int(n1) + int(n2))