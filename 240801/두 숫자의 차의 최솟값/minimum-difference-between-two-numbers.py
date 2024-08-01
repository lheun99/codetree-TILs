n = int(input())
nums = list(map(int, input().split()))

ns = []
for i in nums:
    for j in nums:
        if i - j > 0:
            ns.append(i-j)

print(min(ns))