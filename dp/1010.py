import sys
import math

T = int(sys.stdin.readline())
for i in range(T):
	N, M = map(int, sys.stdin.readline().split())
	print(math.factorial(M) // (math.factorial(N) * math.factorial(M-N)))