import sys
import math

N = int(sys.stdin.readline())
amounts = list(map(int, sys.stdin.readline().split()))

def method1(): # 오른쪽이 꿀벌통
	bee = sum(amounts)
	beehive = N-1
	bee -= amounts[0]

	subtract = math.inf
	tmp = 0
	for i in range(1, N-1):
		subtract = min(tmp + amounts[i]*2, subtract)
		tmp += amounts[i]
	return (bee*2-subtract)

def method2():
	bee = sum(amounts[1:-1])
	return (bee+max(amounts[1:-1]))

def method3(): #왼쪽이 꿀벌통
	bee = sum(amounts)
	beehive = 0
	bee -= amounts[-1]
	subtract = math.inf
	tmp = 0
	for i in range(N-2, 0, -1):
		subtract = min(tmp + amounts[i]*2, subtract)
		tmp += amounts[i]
	return (bee*2-subtract)

print(max(method1(), method2(), method3()))
