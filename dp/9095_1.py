import sys

def func(cur):
	global dp
	if (cur > n):
		return 0
	if (cur == n):
		return 1
	if dp[cur] != 0:
		return dp[cur]
	dp[cur] += func(cur+1)
	dp[cur] += func(cur+2)
	dp[cur] += func(cur+3)
	return dp[cur]

T = int(sys.stdin.readline())
for i in range(T):
	n = int(sys.stdin.readline())
	dp = [0]*11
	print(func(0))
