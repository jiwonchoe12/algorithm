import sys
N = int(sys.stdin.readline())
li = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def dfs(N, length, li):
	if (N <= len(li)):
		print(li[N-1])
	else:
		new = []
		for i in range(length-1, 10):
			for j in li:
				if (int(j[0]) < i):
					new.append(str(i)+j)
				else:
					break
		if (len(new) == 0):
			print(-1)
			exit()
		N -= len(li)
		dfs(N, length+1, new)
	

if (N <= 10):
	print(li[N-1])
else:
	dfs(N, 2, li)
