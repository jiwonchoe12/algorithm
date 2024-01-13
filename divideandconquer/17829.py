import sys

N = int(sys.stdin.readline())
li = []
for i in range(N):
	tmp = list(map(int, sys.stdin.readline().split()))
	li.append(tmp)

def pick(x, y):
	tmp = []
	tmp.append(li[x][y])
	tmp.append(li[x][y+1])
	tmp.append(li[x+1][y])
	tmp.append(li[x+1][y+1])
	tmp.sort()
	return (tmp[-2])


def polling(x, y, len):
	if (len == 2):
		return (pick(int(x), int(y)))
	else:
		tmp = []
		tmp.append(polling(x, y, len//2))
		tmp.append(polling(x, y+len//2, len//2))
		tmp.append(polling(x+len//2, y, len//2))
		tmp.append(polling(x+len//2, y+len//2, len//2))
		tmp.sort()
		return (tmp[-2])
	
print(polling(0, 0, N))