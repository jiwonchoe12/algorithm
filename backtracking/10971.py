import sys
N = int(sys.stdin.readline())
costs = []
for i in range(0, N):
	tmp = list(map(int, sys.stdin.readline().split()))
	costs.append(tmp)

isVisited = [] #방문했는지 체크하는 리스트
for i in range(N):
	isVisited.append(0)
cost = 10000000

def tsp(before, tmp, cnt): #before : 바로 직전의 도시, tmp : 현재까지 저장된 비용, cnt : 지금까지 방문한 도시 개수를 저장
	global start
	global cost
	if (cnt == N - 1): #모든 도시들을 다 돌고 되돌아 온 경우
		if (costs[before][start] != 0):
			tmp += costs[before][start]
			if (tmp < cost):
				cost = tmp
	else:
		for i in range(N):
			if (i != start and isVisited[i] != 1 and costs[before][i] != 0):
				isVisited[i] = 1
				tsp(i, tmp + costs[before][i], cnt + 1)
				isVisited[i] = 0

for i in range(N):
	start = i
	tsp(start, 0, 0)
print(cost)