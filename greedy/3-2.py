'''
n, m, k = map(int, input().split())
num_list = list(map(int, input().split()))

num_list.sort()
a = num_list[-1]
b = num_list[-2]
cnt = 0

i = 1
while (i <= m):
	if (i + k <= m):
		cnt += a * k
		i += k
	else:
		break
	if (i <= m):
		cnt += b
		i += 1
if (i <= m):
	cnt += a * (m - i + 1)

print(cnt)
'''

#더 간단하게 구현
n, m, k = map(int, input().split())
num_list = list(map(int, input().split()))

num_list.sort()
a = num_list[n-1]
b = num_list[n-2]
cnt = 0

#가장 큰 수가 더해지는 횟수
cnt = (m // (k + 1)) * k
cnt += m % (k + 1)

result = cnt * a
result += (m - cnt) * b
print(result)