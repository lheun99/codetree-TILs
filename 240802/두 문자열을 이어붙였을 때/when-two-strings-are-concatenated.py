s = [input() for i in range(2)]

s1 = s[0] + s[1]
s2 = s[1] + s[0]

if s1 == s2:
    print("true")
else:
    print("false")