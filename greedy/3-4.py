n, k = map(int, input().split())
result = 0

i = 0
while (1):
	if (k ** i > n):
		i -= 1
		break
	i += 1
result = i + (n - k ** i)
print(result)