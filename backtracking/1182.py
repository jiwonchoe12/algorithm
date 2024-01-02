import sys

N, S = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))

cnt = 0
def backtrack(tmp, idx):
	global num
	global S
	global cnt
	if (idx == len(num)):
		if (tmp == S):
			cnt += 1
	else:
		backtrack(tmp + num[idx], idx + 1) # 부분 수열에 현재 원소를 포함
		backtrack(tmp, idx + 1) # 부분 수열에 현재 원소를 미포함

backtrack(0, 0)
if (S == 0):
	print(cnt - 1)
else:
	print(cnt)