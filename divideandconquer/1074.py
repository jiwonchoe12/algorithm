import sys

N, r, c = map(int, sys.stdin.readline().split())

cnt = 0
def func(len, i, j):
	global cnt
	if (i == r and j == c):
		return (cnt)
	elif (r < i+len//2 and c < j+len//2):
		return (func(len//2, i, j))
	elif (r <i+len//2 and c >= j+len//2):
		cnt += (len//2)**2
		return(func(len//2, i, j+len//2))
	elif (c < j+len//2):
		cnt += (len//2) * len
		return (func(len//2, i+len//2, j))
	else:
		cnt += (len//2)**2 + (len//2) * len
		return (func(len//2, i+len//2, j+len//2))


print(func(2**N, 0, 0))