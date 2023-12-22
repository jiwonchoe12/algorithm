import sys
N = int(sys.stdin.readline())
A = list(map(int, input().split()))
cal_tmp = list(map(int, input().split()))

big = -1000000000
small = 1000000000
tmp = A[0] #현재까지 계산한 결과 저장
cnt = 1 #몇번째 계산인지
def backtrack(tmp, cnt):
	global big
	global small
	if (cnt == len(A)):
		if (tmp > big):
			big = tmp
		if (tmp < small):
			small = tmp
	else:
		for i in range(0, 4):
			if (cal_tmp[i] != 0):
				cal_tmp[i] -= 1
				if (i == 0): # +
					backtrack(tmp + A[cnt], cnt + 1)
				elif (i == 1): # -
					backtrack(tmp - A[cnt], cnt + 1)
				elif (i == 2): # x
					backtrack(tmp * A[cnt], cnt + 1)
				else: # //
					if (tmp < 0 and A[cnt]):
						backtrack(((tmp * -1) // A[cnt]) * -1, cnt + 1)
					else:
						backtrack(tmp // A[cnt], cnt + 1)
				cal_tmp[i] += 1
backtrack(tmp, cnt)
print(big)
print(small)