#네모를 구성하지 않는 경우만 세기
import sys

N, M = map(int, sys.stdin.readline().split())

def backtrack(position, one):
	global square
	if (position == N * M):
		if (one >= 4):
			for i in range(N - 1):
				for j in range(M - 1):
					if (li[i][j] == 1 and li[i][j + 1] == 1 and li[i + 1][j] == 1 and li[i + 1][j + 1] == 1):
						square += 1
						return
	else:
		x = position // M
		y = position % M
		li[x][y] = 0
		backtrack(position + 1, one)
		li[x][y] = 1
		backtrack(position + 1, one + 1)
	


if (N == 1 or M == 1):
	print(2 ** max(N, M))
else:
	square = 0
	li = [[0 for i in range(M)] for j in range(N)]		
	backtrack(0, 0)
	print(2 ** (N * M) - square)
