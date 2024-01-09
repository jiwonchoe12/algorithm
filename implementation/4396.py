import sys

n = int(sys.stdin.readline())
game = []
for i in range(n):
	game.append(list(sys.stdin.readline()))
player = []
for i in range(n):
	player.append(list(sys.stdin.readline()))
	tmp = []
answer = [['.' for i in range(n)] for j in range(n)] ##초기화


	
def cnt(i, j):
	tmp = 0
	#왼쪽 위 대각선
	if (i != 0 and j != 0 and game[i - 1][j - 1] == '*'):
		tmp += 1
	#위
	if (i != 0 and game[i - 1][j] == '*'):
		tmp += 1
	#오른쪽 위 대각선
	if (i != 0 and j != n - 1 and game[i - 1][j + 1] == '*'):
		tmp += 1
	#왼쪽
	if (j != 0 and game[i][j - 1] == '*'):
		tmp += 1
	#오른쪽
	if (j != n - 1 and game[i][j + 1] == '*'):
		tmp += 1
	#왼쪽 아래 대각선
	if (i != n - 1 and j != 0 and game[i + 1][j - 1] == '*'):
		tmp += 1
	#아래
	if (i != n - 1 and game[i + 1][j] == '*'):
		tmp += 1
	#오른쪽 아래 대각선
	if (i != n - 1 and j != n - 1 and game[i + 1][j + 1] == '*'):
		tmp += 1
	return (tmp)

flag = 0
for i in range(n):
	for j in range(n):
		if (player[i][j] == 'x' and game[i][j] == '.'):
			answer[i][j] = cnt(i, j) #계산해줘야하는경우
		if (player[i][j] == 'x' and game[i][j] == '*'):
			flag = 1
if (flag == 1):
	for i in range(n):
		for j in range(n):
			if (game[i][j] == '*'):
				answer[i][j] = '*'

#정답 출력
for i in range(n):
    print("".join(map(str, answer[i])))
