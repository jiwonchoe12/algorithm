import sys

N = int(sys.stdin.readline())
eggs = []
for i in range(0, N):
	s, w = map(int, sys.stdin.readline().split()) #내구성, 무게
	eggs.append([s, w])

max = 0

def cnt_broke_eggs(eggs):
	cnt = 0
	for i in range(0, N):
		if (eggs[i][0] <= 0): #내구성이 0이하면 깨진 계란
			cnt += 1
	return (cnt)

def is_all_broke(eggs, hand):
	flag = 0
	for i in range(0, N):
		if (i != hand and eggs[i][0] >= 1):
			return (False) #깨지지 않은 계란이 있음
	return (True) #다른 계란이 모두 다 깨짐

def dfs(eggs, hand):
	global max
	if (hand == N):
		#깨진 계란 개수 세기
		tmp = cnt_broke_eggs(eggs)
		if (tmp > max):
			max = tmp #relaxation
	else:
		#손에 있는 계란이 깨졌거나 깨지지 않은 다른 계란이 없다면 넘어가기
		if (eggs[hand][0] <= 0 or is_all_broke(eggs, hand)):
			dfs(eggs, hand+1)
		else:
			#손에 있는 계란이 깨지지 않았으며, 아직 깨지지 않은 다른 계란이 존재
			for i in range(0, N):
				if (i == hand or eggs[i][0] <= 0):
					continue
				#계란 깨기
				eggs[hand][0] -= eggs[i][1] #내구성 감소하기
				eggs[i][0] -= eggs[hand][1]
				dfs(eggs, hand+1) #재귀
				eggs[hand][0] += eggs[i][1] #내구성 증가하기(되돌리기)
				eggs[i][0] += eggs[hand][1]

dfs(eggs, 0)
print(max)		
