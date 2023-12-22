import sys

N = int(sys.stdin.readline())
pos = [] #각 열들의 말들이 어디 행에 들어갈지 position
cnt = 0 #경우의 수를 담는 정답 변수
flag = 0

def nqueen(pos):
	global cnt
	global flag
	if (len(pos) == N):
		cnt += 1
	else:
		for i in range(0, N):
			for j in range(0, len(pos)):
				if (pos[j] == i):
					flag = 1
					break
				if (len(pos) - j == i - pos[j] or len(pos) - j == pos[j] - i):
					flag = 1
					break
			if (flag == 0):
				pos.append(i)
				nqueen(pos)
				pos.pop()
			flag = 0
nqueen(pos)
print(cnt)