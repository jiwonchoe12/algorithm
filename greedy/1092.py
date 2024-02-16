import sys

N = int(sys.stdin.readline())
cranes = list(map(int, sys.stdin.readline().split()))
cranes.sort(reverse=True)
boxNum = int(sys.stdin.readline())
boxes = list(map(int, sys.stdin.readline().split()))
boxes.sort(reverse=True)

if (boxes[0] > cranes[0]):
	print(-1)
	exit()

time = 0
while (len(boxes)):
	for i in range(N):
		if (len(boxes) == 0):
			break
		if (cranes[i] < boxes[-1]):
			break
		for j in range(len(boxes)):
			if (boxes[j] <= cranes[i]):
				boxes.pop(j)
				break
	time += 1
print(time)