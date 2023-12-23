import sys
import collections

N, M = map(int, sys.stdin.readline().split())
li = list(map(int, input().split()))
dic = collections.Counter(li)
dic = dict(sorted(dic.items()))
answer = []

def backtrack(answer):
	if (len(answer) == M):
		print(*answer)
	else:
		for i in dic.keys():
			if (dic[i] == 0):
				continue
			else:
				answer.append(i)
				dic[i] -= 1
				backtrack(answer)
				dic[i] += 1
				answer.pop()

backtrack(answer)