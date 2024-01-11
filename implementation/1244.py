import sys

N = int(sys.stdin.readline())
switch = list(map(int, sys.stdin.readline().split()))
S = int(sys.stdin.readline())
students = []
for i in range(S):
	gender, num = map(int, sys.stdin.readline().split())
	students.append([gender, num])

def change_switch(i):
	if (switch[i] == 0):
		switch[i] = 1
	else:
		switch[i] = 0

for student in students:
	if (student[0] == 1): #남자
		for i in range(1, N + 1):
			if (i % student[1] == 0):
				change_switch(i - 1)
	else: # 여자
		rep = min(student[1] - 1, N - student[1])
		change_switch(student[1] - 1)
		for i in range(1, rep + 1):
			if (switch[student[1] - 1 - i] == switch[student[1] - 1 + i]):
				change_switch(student[1] - 1 - i)
				change_switch(student[1] - 1 + i)
			else:
				break

cnt = 0
for i in switch:
	print(i, end= " ")
	cnt += 1
	if (cnt % 20 == 0):
		print() 
