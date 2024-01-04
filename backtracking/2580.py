import sys

li = []
for i in range(9):
	tmp = list(map(int, sys.stdin.readline().split()))
	li.append(tmp)


def print_answer():
	global li
	for i in range(9):
		print(*li[i])

def checkRow(i, k):
	global li
	for a in range(9):
		if (li[i][a] == k):
			return (True)
	return (False)

def checkCol(j, k):
	global li
	for a in range(9):
		if (li[a][j] == k):
			return (True)
	return (False)

def checkBox(i, j, k):
	global li
	a = i // 3
	b = j // 3
	for row in range(3):
		for col in range(3):
			if (li[a * 3 + row][b * 3 + col] == k):
				return (True)
	return (False)

def dfs(i, j):
	global li
	global flag
	if (i == 9):
		print_answer()
		flag = 1
	else:
		if (li[i][j] != 0):
			# 다음으로 넘어가기
			if (j == 8):
				dfs(i + 1, 0)
				if (flag == 1):
					return 
			else:
				dfs(i, j + 1)
				if (flag == 1):
					return 
		else:
			for k in range(1, 10):
				#같은 가로줄, 세로줄, 박스안 체크
				#True가 반환되면 그 숫자는 불가능
				if (checkRow(i, k) or checkCol(j, k) or checkBox(i, j, k)):
					continue
				li[i][j] = k
				# 다음으로 넘어가기
				if (j == 8):
					dfs(i + 1, 0)
					if (flag == 1):
						return 
				else:
					dfs(i, j + 1)
					if (flag == 1):
						return 
				li[i][j] = 0

flag = 0
dfs(0, 0)