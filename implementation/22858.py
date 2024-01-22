import sys

N, K = map(int, sys.stdin.readline().split())
S = list(map(int, sys.stdin.readline().split()))
D = list(map(int, sys.stdin.readline().split()))

tmp = [0] * N
for _ in range(K):
	for i in range(N):
		tmp[D[i] - 1] = S[i]
	S = tmp[:]
print(*S)