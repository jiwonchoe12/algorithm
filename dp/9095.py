import sys

methods = [0] * 10

for i in range(10):
	if (i == 0):
		methods[i] = 1
	elif (i == 1):
		methods[i] = 2
	elif (i == 2):
		methods[i] = 4
	else:
		methods[i] = methods[i-1] + methods[i-2] + methods[i-3]

T = int(sys.stdin.readline())
for i in range(T):
	n = int(sys.stdin.readline())
	print(methods[n-1])