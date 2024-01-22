import sys

cal = sys.stdin.readline().replace("\n", "")
num = []
oper = []

i = 0
while (i < len(cal)):
	j = i
	while (j < len(cal) and cal[j] != '+' and cal[j] != '-'):
		j += 1
	num.append(int(cal[i:j]))
	if (j < len(cal)):
		oper.append(cal[j])
	i = j+1

while (1):
	try:
		idx = oper.index('+')
		num[idx] = num[idx] + num[idx+1]
		num.pop(idx+1)
		oper.pop(idx)
	except ValueError:
		break
while (1):
	try:
		idx = oper.index('-')
		num[idx] = num[idx] - num[idx+1]
		num.pop(idx+1)
		oper.pop(idx)
	except ValueError:
		break
print(num[0])