i = 1
result_arr = []
while (1):
	l, p, b = map(int, input().split())
	if (l + p + b == 0):
		break
	result = (b // p) * l
	tmp = b % p
	if (tmp > l):
		result += l
	else:
		result += tmp
	result_arr.append(result)

for result in result_arr:
	print("Case %d: %d" %(i, result))
	i += 1