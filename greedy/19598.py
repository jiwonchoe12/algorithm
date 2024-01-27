import sys
import heapq

N = int(sys.stdin.readline())
meetings = []
for _ in range(N):
	start, end = map(int, sys.stdin.readline().split())
	meetings.append([start, end])
meetings = sorted(meetings, key=lambda x:(x[0]))

cnt = 1
hq = []
heapq.heappush(hq, meetings[0][1])
for meeting in meetings[1:]:
	if (meeting[0] >= hq[0]):
		heapq.heappop(hq)
	else:
		cnt += 1
	heapq.heappush(hq, meeting[1])
print(cnt)
