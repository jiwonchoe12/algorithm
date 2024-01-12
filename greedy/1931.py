import sys

N = int(sys.stdin.readline())
li = []
for i in range(N):
	start, end = map(int, sys.stdin.readline().split())
	li.append([start, end])
li.sort(key=lambda x:(x[1], x[0]))

cnt = 1
last_finish = li[0][1]
for i in range(1, N):
	if (li[i][0] >= last_finish):
		cnt += 1
		last_finish = li[i][1]
print(cnt)