from queue import PriorityQueue

q = PriorityQueue()
q1 = PriorityQueue(maxsize = 10)

q.put(3)
q.put(4)
q.put(1)

q1.put((1, 'apple')) #(우선순위, 값) 형태로도 저장 가능
q.get()
q1.get()[1]

import heapq
#최소 힙 구조
#가장 작은 요소가 heap[0]에 위치

hq = []
heapq.heappush(hq, 4)
heapq.heappush(hq, 1)
heapq.heappush(hq, 3)
heapq.heappush(hq, 7)
heapq.heappop(hq) # 1
#비어있으면 IndexError 발생