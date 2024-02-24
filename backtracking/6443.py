import sys

def func():
	global dic
	global tmp
	if (len(tmp) == len(words)):
		for word in tmp:
			print(word, end="")
		print()
	else:
		for i in range(len(dic)):
			if (dic[i][1] != 0):
				tmp.append(dic[i][0])
				dic[i][1] -= 1
				func()
				tmp.pop()
				dic[i][1] += 1

N = int(sys.stdin.readline())
for _ in range(N):
	words = list(sys.stdin.readline().replace("\n", ""))
	words.sort()
	last = 0
	dic = []
	for i in range(len(words)):
		if (words[i] != last):
			dic.append([words[i] ,1])
			last = words[i]
		else:
			dic[-1][1] += 1
	tmp = []
	func()