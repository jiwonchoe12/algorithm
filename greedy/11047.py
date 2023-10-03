n, k = map(int, input().split())
li = [int(input()) for _ in range(n)]

li = li[::-1]
cnt = 0

for coin in li:
	cnt += k // coin
	k %= coin

print(cnt)