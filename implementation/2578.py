import sys

def check_bingo(answer):
	global bingo
	cnt = 0
	tmp = 0
	#가로줄 검사
	for i in range(5):
		for j in range(5):
			if bingo[i][j] in answer:
				tmp += 1
		if (tmp == 5):
			cnt += 1
		tmp = 0

	#세로줄 검사
	for j in range(5):
		for i in range(5):
			if bingo[i][j] in answer:
				tmp += 1
		if (tmp == 5):
			cnt += 1
		tmp = 0

	#대각선 검사
	#(4,0), (3, 1), (2, 2), (1, 3), (0, 4)
	for i in range(5):
		if bingo[i][4-i] in answer:
			tmp += 1
	if (tmp == 5):
		cnt += 1
	tmp = 0

	#대각선 검사
	for i in range(5):
		if bingo[i][i] in answer:
			tmp += 1
	if (tmp == 5):
		cnt += 1
	tmp = 0
	
	if (cnt >= 3):
		return True
	return False

bingo = []
for i in range(5):
	tmp = list(map(int, sys.stdin.readline().split()))
	bingo.append(tmp)

answer = []
cnt = 0
flag = 0
for _ in range(5):
	tmp = list(map(int, sys.stdin.readline().split()))
	if (flag == 1):
		continue
	for i in tmp:
		answer.append(i)
		cnt += 1
		if (check_bingo(answer) == True):
			flag = 1
			break

print(cnt)