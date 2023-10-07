import sys

n = sys.stdin.readline()
if (n[1] >= 'a' and n[1] <= 'h'):
	print("wrong")
else:
	x = int(n[1])
	y = int(ord(n[0]) - ord("a") + 1)
	cnt = 0
	if (x - 1 >= 1 and y + 2 <= 8):
		cnt += 1
	if (x + 1 <= 8 and y + 2 <= 8):
		cnt += 1
	if (x - 1 >= 1 and y - 2 >= 1):
		cnt += 1
	if (x + 1 <= 8 and y - 2 >= 1):
		cnt += 1
	if (x + 2 <= 8 and y + 1 <= 8):
		cnt += 1
	if (x + 2 <= 8 and y - 1 >= 1):
		cnt += 1
	if (x - 2 >= 1 and y + 1 <= 8):
		cnt += 1
	if (x - 2 >= 1 and y - 1 >= 1):
		cnt += 1
	print(cnt)