nums = []

for i in range(4):
    nums.append(list(map(int, input().split())))

res = 0
for a in range(5):
    for j in range(a):
        res += nums[a-1][j]

print(res)