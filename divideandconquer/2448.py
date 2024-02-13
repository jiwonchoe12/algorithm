import sys

N = int(sys.stdin.readline())

arr = [[' ' for i in range(2*N-1)] for j in range(N)]
arr[0][(2*N-1)//2] = '*'
arr[1][(2*N-1)//2-1 : (2*N-1)//2+2] = '* *'
arr[2][(2*N-1)//2-2 : (2*N-1)//2+3] = '*****'

def func(x, y, len):
	if (len == 3):
		return
	else:
		func(x, y, len//2)
		for i in range(len//2):
			arr[x+len//2+i][y-(len-1) : y] = arr[x+i][y-len//2+1 : y+len//2]
			arr[x+len//2+i][y+1 : y+len] = arr[x+i][y-len//2+1 : y+len//2]

func(0, (2*N-1)//2, N)

for i in range(N):
	result = ''
	result = "".join(arr[i])
	print(result)
