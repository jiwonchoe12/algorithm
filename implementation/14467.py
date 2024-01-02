import sys

N = int(sys.stdin.readline())

cnt = [-1] * 11

res = 0
for i in range(N):
	num, loc = map(int, sys.stdin.readline().split())
	if (cnt[num] == -1):
		cnt[num] = loc
	else:
		if (cnt[num] != loc):
			res += 1
			cnt[num] = loc
print(res)