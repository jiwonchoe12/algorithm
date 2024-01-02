import sys
money = int(sys.stdin.readline())
prices = list(map(int, sys.stdin.readline().split())) # 주가

aMoney = money #현금
aStock = 0 #주식
bMoney = money #현금
bStock = 0 #주식

#준현
for price in prices:
	aStock += aMoney // price
	aMoney = aMoney % price

#성민
increase = 0
decrease = 0
before = prices[0]
for price in prices[1:]:
	if (before < price):
		increase += 1
		decrease = 0
	elif(before > price):
		increase = 0
		decrease += 1
	else: #before == price
		increase = 0
		decrease = 0
	if (increase >= 3): #팔아야한다
		bMoney = bMoney + bStock * price
		bStock = 0
	elif (decrease >= 3): #사야한다
		bStock += bMoney // price
		bMoney = bMoney % price

#비교
aTotal = aStock * prices[13] + aMoney
bTotal = bStock * prices[13] + bMoney
if (aTotal > bTotal):
	print("BNP")
elif (aTotal < bTotal):
	print("TIMING")
else:
	print("SAMESAME")