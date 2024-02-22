import sys

def func(depth, conti):
	global dp
	if depth > N:
		return -12341234
	elif conti == 3:
		return -12341234
	elif (depth == N):
		return stairs[depth]
	if dp[depth][conti] != 0:
		return dp[depth][conti]
	dp[depth][conti] = max(dp[depth][conti], func(depth+1, conti+1)+stairs[depth])
	dp[depth][conti] = max(dp[depth][conti], func(depth+2, 1)+stairs[depth])
	return dp[depth][conti]

if __name__ == "__main__":
	N = int(sys.stdin.readline())
	stairs = [0] * (N+1)
	for i in range(1, N+1):
		inpu = int(sys.stdin.readline())
		stairs[i] = inpu
	dp = [[0 for i in range(3)] for j in range(N+1)]
	print(func(0, 0))

