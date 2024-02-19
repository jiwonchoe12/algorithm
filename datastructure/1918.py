import sys

expressions = list(sys.stdin.readline().replace("\n", ""))
stack = []
str = ""
for char in expressions:
	if (char.isalpha()):
		str += char
	elif (char == "("):
		stack.append(char)
	elif (char == '*' or char == '/'):
		while stack and (stack[-1] == '*' or stack[-1] == '/'):
			str += stack.pop()
		stack.append(char)
	elif (char == "+" or char == '-'):
		while stack and stack[-1] != '(':
			str += stack.pop()
		stack.append(char)
	elif (char == ")"):
		while stack[-1] != "(":
			str += stack.pop()
		stack.pop()
while stack:
	str += stack.pop()
print(str)
