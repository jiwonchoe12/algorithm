import sys

def dfs(depth, tmp):
	global answer
	global already_in
	if (depth == 11):
		answer = max(answer, tmp)
	else:
		available = [] #현재 포지션에 가능한 선수들만 저장 -> 재귀수를 줄일 수 있다
		for i in range(11):
			if (arr[i][depth] != 0):
				available.append(i)
		for i in available:
			if (i not in already_in): #이미 현재 포지션에 들어가 있으면 안됨
				already_in.append(i)
				dfs(depth+1, tmp+arr[i][depth])
				already_in.pop()

C = int(sys.stdin.readline())
for _ in range(C):
	answer = 0
	arr = []
	for _ in range(11):
		li = list(map(int, sys.stdin.readline().split()))
		arr.append(li)
	already_in = [] # 이미 선수들이 들어간 포지션을 저장하는 배열
	dfs(0, 0)
	print(answer)