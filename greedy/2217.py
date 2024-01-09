import sys

N = int(sys.stdin.readline())
li = []
for i in range(N):
	tmp = int(sys.stdin.readline())
	li.append(tmp)
li.sort()

answer = li[0] * N
for i in range(1, N):
	tmp = li[i] * (N - i)
	if (tmp > answer):
		answer = tmp
print(answer)