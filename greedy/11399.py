import sys

N = int(sys.stdin.readline())
peoples = list(map(int, sys.stdin.readline().split()))
peoples.sort()

total = 0
tmp = 0 #누적 값
for people in peoples:
	tmp += people
	total += tmp
print(total)