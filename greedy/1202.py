import sys

N, K = map(int, sys.stdin.readline().split())
jewels = []
for _ in range(N):
	M, V = map(int, sys.stdin.readline().split())
	jewels.append([M, V, V/M]) # 무게, 가격, 무게 별 가격

jewels.sort(key = lambda x : (-x[2]))

bags = []
for _ in range(K):
	C = int(sys.stdin.readline())
	bags.append(C)
bags.sort()

prices = 0
for jewel in jewels:
	if (len(bags) == 0):
		break
	for i in range(len(bags)):
		if (bags[i] >= jewel[0]): #보석을 다 넣는경우
			prices += jewel[1]
			bags.pop(i)
			break
print(prices)
