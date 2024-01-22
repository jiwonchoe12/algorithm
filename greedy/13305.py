import sys

N = int(sys.stdin.readline())
roads = list(map(int, sys.stdin.readline().split()))
prices = list(map(int, sys.stdin.readline().split()))
prices.pop()

total = 0
while (1):
	minimum = min(prices)
	idx = prices.index(minimum)
	print(idx)
	total += prices[idx] * sum(roads[idx:])
	if (idx == 0):
		break
	roads = roads[:idx]
	prices = prices[:idx]
print(total)
