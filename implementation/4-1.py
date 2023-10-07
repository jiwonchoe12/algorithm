import sys
n = int(sys.stdin.readline())
moves = list(map(str, sys.stdin.readline().split()))

x = 1
y = 1
for move in moves:
	if (move == "L" and y >= 2):
		y -= 1
	elif (move == "R" and y < n):
		y += 1
	elif (move == "U" and x >= 2):
		x -= 1
	elif (move == "D" and x < n):
		x += 1

print("{} {}".format(str(x), str(y)))