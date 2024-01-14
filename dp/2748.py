import sys

n = int(sys.stdin.readline())
table = [-1] * 91
table[0] = 0
table[1] = 1

def fibo(i):
	if (table[i] != -1):
		return (table[i])
	else:
		table[i] = fibo(i-2) + fibo(i-1)
		return (table[i])
if (n <= 1):
	print(table[n])
else:
	print(fibo(n))