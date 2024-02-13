import sys

def make_queue(i, R):
	global arr
	queue = []
	dx = [0, 1, 0, -1]
	dy = [1, 0, -1, 0]
	row = (M-2*i)-1#가로
	col = (N-2*i)-1#세로
	x, y = i, i

	#큐 만들기
	for j in range(4):
		if (j % 2 == 0):
			rep = row
		else:
			rep = col
		for _ in range(rep):
			queue.append(arr[x][y])
			x += dx[j]
			y += dy[j]
	#위치 옮기기
	queue = queue[R % (2 * (row + col)) : ] + queue[: R % (2 * (row + col))]
	#제자리에 값 넣기
	x, y, cnt = i, i, 0
	for j in range(4):
		if (j % 2 == 0):
			rep = row
		else:
			rep = col
		for _ in range(rep):
			arr[x][y] = queue[cnt]
			x += dx[j]
			y += dy[j]
			cnt += 1

#입력	
N, M, R = map(int, sys.stdin.readline().split()) #N:세로, M:가로
arr = []
for _ in range(N):
	li = list(map(int, sys.stdin.readline().split()))
	arr.append(li)
#링개수 만큼 반복
rep = min(N, M) // 2
for i in range(rep):
	make_queue(i, R)
#출력
for i in range(N):
	for j in range(M):
		print(arr[i][j], end=" ")
	print()