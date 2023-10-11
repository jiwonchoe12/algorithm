import sys
import heapq

v, e = map(int, sys.stdin.readline().split())
visited = [False] * (v + 1) # 1 ~ v까지 사용할 것이기에 크기를 (v+1)만큼 생성한다
weights = [[] for _ in range(v + 1)]

for i in range(e):
	a, b, c = map(int, sys.stdin.readline().split())
	weights[a].append([c, b]) #내 노드에서 갈수 있는 노드(b)와 그 가중치 값(c)를 저장한다
	weights[b].append([c, a])

heap = [[0, 1]] #1번 노드가 시작 노드

answer = 0 #최소 스패닝 트리의 가중치
cnt = 0 #반복 횟수 => 간선을 v-1개 찾으면 알고리즘은 중단된다

while True:
	print(heap)
	if (cnt == v):
		break
	c, a = heapq.heappop(heap)
	if not visited[a]: #위에서 pop을 해서 heap에는 사라졌다. 따라서 만약 방문했다면 버려진다.
		visited[a] = True #방문을 하지 않았다면 가장 최적의 선택이다. 왜냐하면 pop에서 weight가 가장 작은 간선이 뽑혔기 때문에
		answer += c
		cnt += 1
		for i in weights[a]:
			heapq.heappush(heap, i)

print(answer)