import sys

def backtrack(last):
	if (len(answer) == M):
		print(*answer)
	else:
		for i in range(last, N + 1):
			answer.append(i)
			backtrack(i)
			answer.pop()

N, M = map(int, sys.stdin.readline().split())
answer = []
backtrack(1)
