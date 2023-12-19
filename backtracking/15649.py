import sys
n, m = map(int, sys.stdin.readline().split())

answer = []
def backtrack(answer):
	if (len(answer) ==  m):
		print(*answer)
	else:
		for i in range (1, n + 1):
			if (i not in answer):
				answer.append(i)
				backtrack(answer)
				answer.pop()

backtrack(answer)