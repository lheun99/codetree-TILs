s = input()
c = input()

cnt = 0
for i in range(len(s)):
    if c == s[i:i+len(c)]:
        cnt += 1

print(cnt)