import sys

N = int(sys.stdin.readline())

answer = []


def check(num):
	if (len(answer) <= 2):
		return (True)
	answer.append(num)
	rep = len(answer) // 2 #1
	for i in range(2, rep + 1):
		cnt = 0
		for j in range(len(answer) - i * 2, len(answer) - i):
			if (answer[j] != answer[j + i]):
				break
			else:
				cnt += 1
		if (cnt == i):
			answer.pop()
			return (False)
	answer.pop()
	return (True)

def dfs(last):
	if (len(answer) == N):
		for i in answer:
			print(i, end='')
		exit()
	else:
		for i in range(1, 4):
			if (last == i):
				continue
			elif (check(i) == True):
				answer.append(i)
				dfs(i)
				answer.pop()

dfs(0)
