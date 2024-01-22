import sys

k = int(sys.stdin.readline())
def log2(n):
	cnt = 1
	while (True):
		if (n <= cnt):
			return (cnt//2)
		else:
			cnt = cnt * 2

rep = 0
while (k != 1):
	rep += 1
	k = k - log2(k)


if (rep % 2 == 0):
	print(0)
else:
	print(1)