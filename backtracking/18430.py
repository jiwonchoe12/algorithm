import sys

N, M = map(int, sys.stdin.readline().split())
arr = []
for _ in range(N):
	li = list(map(int, sys.stdin.readline().split()))
	arr.append(li)

flag = [[0 for _ in range(M)] for _ in range(N)]

def make_boomerang1(i, j):
	if (i+1 < N and j-1 > -1 and flag[i+1][j] == 0 and flag[i][j-1] == 0):
		flag[i+1][j] = 1
		flag[i][j-1] = 1
		flag[i][j] = 1
		return (True)
	return (False)

def make_boomerang2(i, j):
	if (i-1 > -1 and j-1 > -1 and flag[i-1][j] == 0 and flag[i][j-1] == 0):
		flag[i-1][j] = 1
		flag[i][j-1] = 1
		flag[i][j] = 1
		return (True)
	return (False)

def make_boomerang3(i, j):
	if (i-1 > -1 and j+1 < M and flag[i-1][j] == 0 and flag[i][j+1] == 0):
		flag[i-1][j] = 1
		flag[i][j+1] = 1
		flag[i][j] = 1
		return (True)
	return (False)

def make_boomerang4(i, j):
	if (i+1 < N and j+1 < M and flag[i+1][j] == 0 and flag[i][j+1] == 0):
		flag[i+1][j] = 1
		flag[i][j+1] = 1
		flag[i][j] = 1
		return (True)
	return (False)

max = 0
def backtrack(idx, tmp):
	global flag
	global max
	if (idx == N*M):
		if (tmp > max):
			max = tmp
	else:
		i = idx // M
		j = idx % M
		if (flag[i][j] == 1):
			backtrack(idx+1, tmp)
		else:
			if (make_boomerang1(i, j)):
				backtrack(idx+1, tmp + (arr[i][j] * 2 + arr[i+1][j] + arr[i][j-1]))
				flag[i+1][j] = 0
				flag[i][j-1] = 0
				flag[i][j] = 0
			if (make_boomerang2(i, j)):
				backtrack(idx+1, tmp + (arr[i][j] * 2 + arr[i-1][j] + arr[i][j-1]))
				flag[i-1][j] = 0
				flag[i][j-1] = 0
				flag[i][j] = 0
			if (make_boomerang3(i, j)):
				backtrack(idx+1, tmp + (arr[i][j] * 2 + arr[i-1][j] + arr[i][j+1]))
				flag[i-1][j] = 0
				flag[i][j+1] = 0
				flag[i][j] = 0
			if (make_boomerang4(i, j)):
				backtrack(idx+1, tmp + (arr[i][j] * 2 + arr[i+1][j] + arr[i][j+1]))
				flag[i+1][j] = 0
				flag[i][j+1] = 0
				flag[i][j] = 0
			backtrack(idx+1, tmp)

backtrack(0, 0)
print(max)

