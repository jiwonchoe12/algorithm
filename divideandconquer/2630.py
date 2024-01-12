import sys

N = int(sys.stdin.readline())
paper = []
for i in range(N):
	inpu = list(map(int, sys.stdin.readline().split()))
	tmp = []
	for a in inpu:
		if (a != ' '):
			tmp.append(a)
	paper.append(tmp)

white = 0
blue = 0

def all_same(x, y, len):
	global white
	global blue
	color = paper[x][y]
	if (len != 1):
		for i in range(len):
			for j in range(len):
				if (paper[x + i][y + j] != color):
					return (False)
	if (color == 1): #파란색
		blue += 1
	else:
		white += 1
	return (True)

def divide_and_conquer(x, y, len): #왼쪽 끝 좌표, 길이
	global white
	global blue
	if (all_same(x, y, len) == False):
		divide_and_conquer(x, y, len//2)
		divide_and_conquer(x + len//2, y, len//2)
		divide_and_conquer(x, y + len//2, len//2)
		divide_and_conquer(x + len//2, y + len//2, len//2)


divide_and_conquer(0, 0, N)
print(white)
print(blue)