import sys

N, M = map(int, sys.stdin.readline().split())
arr = [[0 for i in range(M)] for j in range(N)]

cnt = 0

def can_check(i, j):
	if (i == 0 or j == 0):
		return (True)
	if (arr[i][j-1] == 1 and arr[i-1][j] == 1 and arr[i-1][j-1] == 1):
		return (False)
	return (True)

def dfs(idx):
	global cnt
	if (idx == N*M):
		cnt += 1
	else:
		if (can_check(idx//M, idx%M)):
			arr[idx//M][idx%M] = 1
			dfs(idx+1)
			arr[idx//M][idx%M] = 0
		dfs(idx+1)

dfs(0)
print(cnt)