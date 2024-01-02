import sys

str = sys.stdin.readline().strip()
board = list(str)

start = 0
end = 1
flag = 0
while (1):
	while (start != len(board) and board[start] != 'X'):
		start += 1
	while (end != len(board) and (not(board[end - 1] == 'X' and board[end] == '.'))):
		end += 1
	length = end - start
	if (length % 2 != 0):
		flag = 1
		break
	for i in range(0, length // 4):
		board[start] = 'A'
		board[start + 1] = 'A'
		board[start + 2] = 'A'
		board[start + 3] = 'A'
		start += 4
	if (length % 4 != 0):
		board[start] = 'B'
		board[start + 1] = 'B'
	if (len(board) == end):
		break
	start = end
	end += 1

if (flag == 1):
	print(-1)
else:
	for i in board:
		print(i, end = '')
	print()