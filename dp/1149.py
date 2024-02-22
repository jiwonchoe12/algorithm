import sys
import math

sys.setrecursionlimit(10**6)

def func(pos, color):
	global dp
	if (pos == N):
		return (0)
	
	if (dp[pos][color] != math.inf):
		return (dp[pos][color])
	for i in range(1, 4):
		if (i != color):
			dp[pos][color] = min(dp[pos][color], houses[pos][i] + func(pos+1, i))
	return dp[pos][color]


if (__name__ == "__main__"):
	N = int(sys.stdin.readline())
	houses = []
	dp = [[math.inf for i in range(4)] for i in range(N)]
	for _ in range(N):
		red, blue, green = map(int, sys.stdin.readline().split())
		houses.append([0, red, blue, green])
	
	print(func(0, 0))