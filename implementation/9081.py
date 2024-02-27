import sys
import copy

def func():
	global original_word
	last = original_word[-1]
	for i in range(len(original_word)-2, -1, -1):
		if (original_word[i] >= last):
			last = original_word[i]
		else:
			tmp = copy.deepcopy(original_word[i+1:])
			tmp.sort()
			for j in range(len(tmp)):
				if (tmp[j] > original_word[i]):
					original_word[i], tmp[j] = tmp[j], original_word[i]
					break
			tmp.sort()
			original_word[i+1:] = tmp[::]
			break
	print("".join(original_word))

T = int(sys.stdin.readline())
for _ in range(T):
	li = list(sys.stdin.readline().replace("\n", ""))
	original_word = copy.deepcopy(li)
	li.sort(reverse=True)
	if (original_word == li):
		print("".join(original_word))
	else:
		func()