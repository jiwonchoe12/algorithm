import sys

def dfs(last, cnt):
	global alpha
	global res
	if (cnt == K - 5):
		tmp = 0
		for word in words:
			can_make = True
			for w in word:
				if (alpha[ord(w) - ord('a')] == False):
					can_make = False
					break
			if (can_make):
				tmp += 1
		res = max(res, tmp)
	else:
		for i in range(last, 26):
			if not alpha[i]: # 아직 추가가 되지 않았다면
				alpha[i] = True
				dfs(i+1, cnt+1)
				alpha[i] = False

N, K = map(int, sys.stdin.readline().split())

words = []
for i in range(N):
	word = sys.stdin.readline().replace("\n", "")
	word = set(word) - {'a', 'n', 't', 'i', 'c'}
	words.append(list(word))

if (K < 5):
	print(0)
	exit()

res = 0
alpha = [False] * 26
for c in ('a', 'n', 't', 'i', 'c'):
	alpha[ord(c) - ord('a')] = True

dfs(0, 0)
print(res)