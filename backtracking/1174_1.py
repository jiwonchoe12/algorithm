import sys

N = int(sys.stdin.readline())

li = []
def dfs(first, num):
	li.append(num)
	if (num % 10 == 0):
		return
	else:
		for i in range(0, first):
			dfs(i, num * 10 + i)

for i in range(10):
	dfs(i, i)
li.sort()
if (len(li) < N):
	print(-1)
else:
	print(li[N-1])

'''
#맨 앞자리 수를 전달하지 않고 함수 안에서 모든 경우를 다 구하는 경우
arr = [] #임시 저장 변수
result = set()
def dfs():
	if (len(arr) > 0):
		#map() 함수는 여러 개의 데이터를 받아서 각각의 요소에 함수를 적용한 결과를 반환하는 내장 함수입니다.
		#리스트, 튜플 등의 반복 가능한(iterable) 객체를 입력으로 받을 수 있습니다.
		#''.join(리스트)를 이용하면 매개변수로 들어온 ['a', 'b', 'c'] 이런 식의 리스트를 'abc'의 문자열로 합쳐서 반환해주는 함수
		result.add(int("".join(map(str, arr))))
	for i in range(10):
		if (len(arr) == 0 or arr[-1] > i): #현재 넣으려는 값보다 마지막 값이 더 큰 경우
			arr.append(i)
			dfs()
			arr.pop()

try:
	dfs()
	result = list(result)
	result.sort()
	print(result[N-1])
except:
	print(-1)
'''