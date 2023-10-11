import sys

n = int(sys.stdin.readline())
people = []
for i in range(n):
	x, y = map(int, sys.stdin.readline().split())
	people.append([x, y])


for i in range(n):
	rank = 1
	for j in range(n):
		if (people[i][0] < people[j][0] and people[i][1] < people[j][1]):
			rank += 1
	print(rank, end = " ")
