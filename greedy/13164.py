import sys
n, k = map(int, sys.stdin.readline().split())

nums =list( map(int, sys.stdin.readline().split()))
gap = []
for i in range(1, n):
	gap.append(nums[i] - nums[i - 1])

gap.sort()
sum = 0
if (n != k):
	for i in range(n - k):
		sum += gap[i]
print(sum)
