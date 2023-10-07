import sys

n = int(sys.stdin.readline())

cnt = 0
for i in range(n+1):
	str_i = str(i)
	if (str_i.find('3') != -1):
		cnt += 3600
		continue
	for j in range(60):
		str_j = str(j)
		if (str_j.find('3') != -1):
			cnt += 60
		else :
			cnt += 15
print(cnt)