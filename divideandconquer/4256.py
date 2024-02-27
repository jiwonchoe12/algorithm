import sys

def postorder(order, idx):
	if (len(order) == 0):
		return 
	if (len(order) == 1):
		print(order[0], end=" ")
	else:
		id = order.index(preorder[idx])
		postorder(order[:id], idx+1)
		postorder(order[id+1:], idx+len(order[:id])+1)
		print(order[id], end=" ")

T = int(sys.stdin.readline())
for _ in range(T):
	n = int(sys.stdin.readline())
	preorder = list(map(int, sys.stdin.readline().split()))
	inorder = list(map(int, sys.stdin.readline().split()))
	postorder(inorder, 0)
	print()