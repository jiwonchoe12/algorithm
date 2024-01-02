import sys

n = int(sys.stdin.readline())

cnt5 = n // 5
flag = 0

while (cnt5 >= 0):
	left = n - cnt5 * 5
	if (left % 2 == 0):
		flag = 1
		break
	cnt5 -= 1

if (flag == 1):
	print(left // 2 + cnt5)
else:
	print(-1)