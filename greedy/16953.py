import sys

A, B = map(int, sys.stdin.readline().split())
tmp = B
cnt = 0

while (tmp > A):
	if ((tmp - 1) % 10 == 0): #끝자리가 1이라면
		tmp = (tmp - 1) / 10
		cnt += 1
	elif (tmp % 2 == 0):
		tmp = tmp / 2
		cnt += 1
	else:
		break
if (tmp == A):
	print(cnt + 1)
else:
	print(-1)
