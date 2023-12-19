import sys
n, m = map(int, sys.stdin.readline().split())

answer = []
def backtrack(answer, s):
	if (len(answer) ==  m):
		print(*answer)
	else:
		for i in range (s, n + 1):
			answer.append(i)
			backtrack(answer, i + 1)
			answer.pop()

backtrack(answer, 1)