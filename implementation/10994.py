import sys

N = int(sys.stdin.readline())
row = 2 * N - 2 #몇행인지(세로)
col = 4 * N - 3#몇열인지(가로)
li = [[0 for i in range(col)] for j in range(row)]
for i in range(row):
	depth = i // 2
	for k in range(depth):
		li[i][2 * k] = '*'
		li[i][2 * k + 1] = ' '
	if (i % 2 == 0):
		for k in range(2*depth, col-2*depth):
			li[i][k] = '*'
	else:
		li[i][2*depth] = '*'
		for k in range(2*depth + 1, col-2*depth - 1):
			li[i][k] = ' '
		li[i][col - 2*depth - 1] = '*'		
	for k in range(depth):
		li[i][col-2*k - 2] = ' '
		li[i][col-2*k - 1] = '*'



#윗부분 출력
for i in range(row):
	for j in range(col):
		print(li[i][j], end ='')
	print()
#중간 출력
for i in range(col):
	if (i % 2 == 0):
		print('*', end ='')
	else:
		print(' ', end ='')
print()
#아랫부분 출력
for i in range(row-1, -1, -1):
	for j in range(col):
		print(li[i][j], end ='')
	print()