import sys
import copy

n, m = map(int, sys.stdin.readline().split())
x, y, dir = map(int, sys.stdin.readline().split())
maps = []
for i in range(n):
	maps.append(list(map(int, sys.stdin.readline().split())))
check = copy.deepcopy(maps)
check[x][y] = 2

left_dir = [3, 0, 1, 2]
move_x = [0, -1, 0, 1]
move_y = [-1, 0, 1, 0]

while (True):
	i = 1
	while (i < 4):
		if (check[x + move_x[dir]][y + move_y[dir]] == 0):
			x += move_x[dir]
			y += move_y[dir]
			check[x][y] = 2
			dir = left_dir[dir]
			break
		else:
			dir = left_dir[dir]
			i += 1
	if (i == 4):
		if (dir == 0):
			x += 1
		elif (dir == 1):
			y -= 1
		elif (dir == 2):
			x -= 1
		elif (dir == 3):
			y += 1
		if (check[x][y] != 0):
			break

cnt = 0
for i in range(n):
	cnt += check[i].count(2)
print(cnt)