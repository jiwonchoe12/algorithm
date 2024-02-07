import sys
import math

n = int(sys.stdin.readline())

dp = [0] * (n+1)
i = 0
while (i*i <= n):
	dp[i*i] = 1
	i += 1

for i in range(2, n+1):
	if (dp[i] != 0):
		continue
	minimum = math.inf
	j = 1
	while (j * j <= i):
		minimum = min(minimum, dp[j*j] + dp[i - j*j])
		j += 1
	dp[i] = minimum
print(dp[n])