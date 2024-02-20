import sys

N = int(sys.stdin.readline())
schedule = [0] * 366
for _ in range(N):
	start, end = map(int, sys.stdin.readline().split())
	for i in range(start, end+1):
		schedule[i] += 1

i = 1
area = 0
while (i < 366):
	if (schedule[i] != 0):
		height = 0
		start = i
		while (i < 366 and schedule[i] != 0):
			height = max(height, schedule[i])
			i += 1
		area += (i - start) * height
	else:
		i += 1

print(area)