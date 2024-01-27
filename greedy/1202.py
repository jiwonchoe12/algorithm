import sys
import heapq

N, K = map(int, sys.stdin.readline().split())
jewels = []
for _ in range(N):
	M, V = map(int, sys.stdin.readline().split())
	jewels.append([M, V]) # 무게, 가격

jewels.sort() #무게 낮은 순으로 정렬

bags = []
for _ in range(K):
	C = int(sys.stdin.readline())
	bags.append(C)
bags.sort() #무게 낮은 순으로 정렬

prices = 0
max_heap = [] #가방에 담을 수 있는 주얼리를 저장
bag_idx = 0
jewel_idx = 0

while (bag_idx < K):
	if (jewel_idx < N and bags[bag_idx] >= jewels[jewel_idx][0]): #가방에 담을 수 있다면
		heapq.heappush(max_heap, (-jewels[jewel_idx][1], jewels[jewel_idx][1]))
		jewel_idx += 1
	else:
		if (len(max_heap) != 0):
			prices += heapq.heappop(max_heap)[1]
		bag_idx += 1
print(prices)