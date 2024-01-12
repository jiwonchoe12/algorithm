import sys

li = list(sys.stdin.readline().rstrip('\n')) #rstrip('\n') : 문자열 오른쪽 개행 제거

zero = 0
one = 0

last = '-1'
for i in li:
	if (i != last):
		last = i
		if (i == '0'):
			zero += 1
		else:
			one += 1

print(min(zero, one))