import sys

N, M = map(int, sys.stdin.readline().split())
tmp = list(map(int, sys.stdin.readline().split()))
tmp.sort()

li = []
last = 0
for now in tmp:
	if (last != now):
		li.append(now)
		last = now

answer = []
def dfs(last): #매개변수는 last index
	if (len(answer) == M):
		print(*answer)
	else:
		for i in range(last, len(li)):
			answer.append(li[i])
			dfs(i)
			answer.pop()

dfs(0)
