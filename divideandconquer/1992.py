import sys

N = int(sys.stdin.readline())
arr = []
for _ in range(N):
	line = list(sys.stdin.readline())
	arr.append(line)

def all_same(x, y, len):
	flag = arr[x][y]
	for i in range(len):
		for j in range(len):
			if (arr[x+i][y+j] != flag):
				return (False)
	return (True)

def func(x, y, len):
	if (all_same(x, y, len)):
		print(arr[x][y], end="")
	elif (len==2):
		print("(", end="")
		print(arr[x][y], end="")
		print(arr[x][y+1], end="")
		print(arr[x+1][y], end="")
		print(arr[x+1][y+1], end="")
		print(")", end="")
	else:
		print("(", end="")
		func(x, y, len//2)
		func(x, y+len//2, len//2)
		func(x+len//2, y, len//2)
		func(x+len//2, y+len//2, len//2)
		print(")", end="")

func(0, 0, N)