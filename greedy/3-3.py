n, m = map(int, input().split()) #행, 열
arr = [list(map(int, input().split())) for _ in range(n)]

ret = -1
for i in range(n):
	arr[i].sort()
	if (ret == -1):
		ret = arr[i][0]
	elif (ret < arr[i][0]):
		ret = arr[i][0]

print(ret)