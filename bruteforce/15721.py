import sys

A = int(sys.stdin.readline())
T = int(sys.stdin.readline())
word = int(sys.stdin.readline())

people = -1
def func():
	global people
	cnt = 0
	n = 1 #회차
	while (True):
		for i in range(2):
			cnt += 1
			if (cnt == T and word == 0):
				people += 1
				return
			people += 2
			if (cnt == T and word == 1):
				return
		for i in range(n+1):
			if (word == 0):#0
				cnt += 1
			people += 1
			if (cnt == T):
				return
		for i in range(n+1):
			if (word == 1):#1
				cnt += 1
			people += 1
			if (cnt == T):
				return
		n += 1
func()
print(people % A)
'''
0 1 2 3

0 1 0 1
0 0 1 1
0 1 0 1
0 0 0 1
1 1
'''