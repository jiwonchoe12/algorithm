import sys

board = []
player1 = 0
player2 = 0
for _ in range(3):
	li = list(map(int, sys.stdin.readline().split()))
	player1 += li.count(1)
	player2 += li.count(2)
	board.append(li)

if (player1 == player2):
	player = 1
	not_player = 2
else:
	player = 2
	not_player = 1
print("player", player)
win = 10 #내가 이기는 가장 빠른 시기
lose = 10 #상대편이 이기는 가장 빠른 시기

def is_win():
	global board
	for i in range(3): #행 확인
		if (board[i][0] != 0 and board[i][0] == board[i][1] and board[i][1] == board[i][2]):
			print(1)
			return (True)
	for i in range(3): #열 확인
		if (board[0][i] != 0 and board[0][i] == board[1][i] and board[1][i] == board[2][i]):
			print(2)
			return (True)
	#대각선 확인(00, 11, 22)
	if (board[0][0] != 0 and board[0][0] == board[1][1] and board[1][1] == board[2][2]):
		print(3)
		return (True)
	#대각선 확인(20, 11, 02)
	if (board[2][0] != 0 and board[2][0] == board[1][1] and board[1][1] == board[0][2]):
		print(4)
		return (True)
	return (False)

def dfs(depth):
	global board
	global win
	global lose
	if (is_win()):
		print("yes")
		if (depth % 2 == 0): #상대방이 이긴경우
			lose = min(lose, depth)
		else: #내가 이긴경우
			win = min(win, depth)
	else:
		for i in range(3):
			for j in range(3):
				if (board[i][j] == 0):
					#depth가 짝수이면 player가 현재 진행중
					#depth가 홀수이면 상대방이 현재 진행중
					if (depth % 2 == 0):
						board[i][j] = player
					else:
						board[i][j] = not_player
					dfs(depth+1)
					board[i][j] = 0

dfs(0)
if (win == 10 and lose == 10):
	print("D")
elif (win > lose):
	print("L")
else:
	print("W")