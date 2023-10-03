#설탕 배달
n = int(input())

five = n // 5
three = 0
result = -1

while (five >= 0):
	left = n - five * 5
	if (left % 3 == 0):
		result = left // 3 + five
		break
	five -= 1

print(result)