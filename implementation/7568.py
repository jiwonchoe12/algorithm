#다시하기
import sys

n = int(sys.stdin.readline())
people = []
for i in range(n):
	x, y = map(int, sys.stdin.readline().split())
	people.append([i, x, y, 0])

people.sort(key = lambda x:(-x[1], -x[2]))
print(people)
rank = 1
cnt = 1
people[0][3] = rank
for i in range(1, n):
	if (people[i-1][1] > people[i][1] and people[i - 1][2] > people[i][2]):
		rank += cnt
		cnt = 1
	else:
		cnt += 1
	people[i][3] = rank

people.sort()

for i in range(n):
	print(people[i][3], end=" ")
