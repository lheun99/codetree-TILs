s = input()

res = ""
for i in s:
    if i.isupper():
        res += i.lower()
    elif i.islower():
        res += i.upper()
print(res)