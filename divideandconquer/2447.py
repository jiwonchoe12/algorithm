import sys
import math

N = int(sys.stdin.readline())
pattern = [[' ' for i in range(N)] for j in range(N)]

base = []
base.append("***")
base.append("* *")
base.append("***")

def func(x, y, len):
	global pattern
	if (len == 3):
		for i in range(3):
			pattern[x + i][y : y+3] = base[i][0:3]
	else:
		func(x, y, len//3)
		for i in range(len//3):
			pattern[x+i][len//3:len//3*2] = pattern[x+i][0:len//3]
			pattern[x+i][len//3*2:] = pattern[x+i][0:len//3]
			pattern[x+len//3+i][0:len//3] = pattern[x+i][0:len//3]
			pattern[x+len//3+i][len//3*2:] = pattern[x+i][0:len//3]
			pattern[x+len//3*2+i][0:len//3] = pattern[x+i][0:len//3]
			pattern[x+len//3*2+i][len//3:len//3*2] = pattern[x+i][0:len//3]
			pattern[x+len//3*2+i][len//3*2:] = pattern[x+i][0:len//3]

func(0, 0, N)
#출력
for i in range(N):
	str = ''
	for j in range(N):
		str += pattern[i][j]
	print(str)
