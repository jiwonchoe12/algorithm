import sys

N, M = map(int, sys.stdin.readline().split())
if (N == 1 or M == 1):
	print(2 ** max(N, M))
else:
	case = N - 1 + M - 2
	choice = N * M - 4
	square = case #2x2 정사각형만 선택
	for i in range(choice): #정사각형 이외에 선택할 수 있는 개수
