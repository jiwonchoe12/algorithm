import sys
import math

N = list(sys.stdin.readline().replace("\n", ""))
maximum = -math.inf
minimum = math.inf

def cnt_odd(arr):
	cnt = 0
	for i in arr:
		if int(i) % 2 == 1: #홀수라면
			cnt += 1
	return (cnt)

def func(arr, tmp):
	global maximum
	global minimum
	if (len(arr) == 1):
		maximum = max(maximum, tmp)
		minimum = min(minimum, tmp)
	elif (len(arr) == 2):
		arr = list(str(int(arr[0]) + int(arr[1]))) 
		func(arr, tmp + cnt_odd(arr))
	else:
		for i in range(1, len(arr)-1):
			for j in range(i+1, len(arr)):
				num = int("".join(arr[0:i])) + int("".join(arr[i:j])) + int("".join(arr[j:]))
				func(list(str(num)), tmp + cnt_odd(list(str(num))))
				
func(N, cnt_odd(N)) #현재까지 얻은 홀수 개수
print(minimum, end=" ")
print(maximum)