import sys

n = int(sys.stdin.readline())
table = [] #tabulation
table.append(0)
table.append(1)
for i in range(2, n+1):
	table.append(table[i-2] + table[i-1])
print(table[n])