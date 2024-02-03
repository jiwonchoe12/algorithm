import sys
N = int(sys.stdin.readline()) #센서 개수
K = int(sys.stdin.readline()) #집중국 개수 #집중국을 세워야한다
censors = list(map(int, sys.stdin.readline().split()))
censors.sort()

gap = []
for i in range(1, N):
	gap.append(censors[i] - censors[i-1])
gap.sort()
print(sum(gap[:N-K]))