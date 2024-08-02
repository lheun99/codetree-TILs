from collections import deque

s = input()

deq = deque()
for idx, j in enumerate(s):
    if (idx+1) % 2 == 0:
        deq.appendleft(j)

for i in deq:
    print(i, end = "")