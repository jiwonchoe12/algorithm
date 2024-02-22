import sys

N = int(sys.stdin.readline())
stairs = []
for _ in range(N):
	input = int(sys.stdin.readline())
	stairs.append(input)
dp = [0] * N

for i in range(N):
	if (i == 0):
		dp[i] = stairs[i]
	elif (i == 1):
		dp[i] = max(stairs[i] + stairs[i-1], stairs[i])
	elif (i == 2):
		dp[i] = max(stairs[i] + stairs[i-2], stairs[i] + stairs[i-1])
	else:
		dp[i] = max(dp[i-2], dp[i-3] + stairs[i-1]) + stairs[i]
print(dp[N-1])