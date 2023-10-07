#우선순위 큐
import heapq
import sys

n = int(sys.stdin.readline())

q = []
for i in range(n):
	start, end = map(int, sys.stdin.readline().split())
	q.append([start, end])

q.sort() #q[i][0] 기준으로 오름차순으로 정렬이 된다

room = []
heapq.heappush(room, q[0][1])

for i in range(1, n):
	if (q[i][0] < room[0]): #현재 회의실 끝나는 시간보다 다음 회의 시작 시간이 빠르면
		heapq.heappush(room, q[i][1]) #새로운 회의실 개설
	else: #현재 회의실에 이어서 회의 개최 가능
		heapq.heappop(room) #새로운 회의로 시간 변경을 위해 pop 후 새 시간 push
		heapq.heappush(room, q[i][1])

print(len(room))