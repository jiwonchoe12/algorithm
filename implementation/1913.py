import sys
import math

N = int(sys.stdin.readline())
find = int(sys.stdin.readline())

li = [[0 for i in range(N)] for j in range(N)]
loc_x = 0
loc_y = 0
x = 0
y = 0

num = N * N
for i in range(N//2):
	rep = int(math.sqrt(num))
	#아래로 내려가기
	for j in range(rep - 1):
		li[x][y] = num
		if (num == find):
			loc_x = x + 1
			loc_y = y + 1
		num -= 1
		x += 1
	#오른쪽으로 가기
	for j in range(rep - 1):
		li[x][y] = num
		if (num == find):
			loc_x = x + 1
			loc_y = y + 1
		num -= 1
		y += 1
	#위로 가기
	for j in range(rep - 1):
		li[x][y] = num
		if (num == find):
			loc_x = x + 1
			loc_y = y + 1
		num -= 1
		x -= 1
	#왼쪽으로 가기
	for j in range(rep - 1):
		li[x][y] = num
		if (num == find):
			loc_x = x + 1
			loc_y = y + 1
		num -= 1
		y -= 1
	x += 1
	y += 1
li[x][y] = 1
if (find == 1):
	loc_x = x + 1
	loc_y = y + 1

for i in range(N):
	print(*li[i])
print(loc_x, loc_y)
