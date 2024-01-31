import sys

N = int(sys.stdin.readline())
roads = list(map(int, sys.stdin.readline().split()))
prices = list(map(int, sys.stdin.readline().split()))
prices.pop()

dis = sum(roads)
last = 0
total = 0

for i in range(N-1):
	if (last == 0 or prices[i] < last):
		total += dis * (prices[i] - last)
		last = prices[i]
	dis -= roads[i]
print(total)
