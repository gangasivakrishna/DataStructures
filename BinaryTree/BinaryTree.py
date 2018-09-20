#Binary Tree

#Node Creation
class Node:

	def __init__(self,key):

		self.left = None

		self.right = None

		self.val = key

#preorder

def preorder(root):

	if root:

		print(root.val,end = ' ')

		preorder(root.left)

		preorder(root.right)

#postorder

def postorder(root):

	if root:

		postorder(root.left)

		postorder(root.right)

		print(root.val,end = ' ')

#inorder

def inorder(root):

	if root:

		inorder(root.left)

		print(root.val,end = ' ')

		inorder(root.right)

# bft

def bft(root):

	if root is None:

		print("No Tree to Traversal")

	else:

		queue = []

		queue.append(root)

		while(len(queue)>0):

			root = queue[0]

			print(root.val,end = ' ')

			node = queue.pop(0)
			
			if node.left is not None:

				queue.append(node.left)

			if node.right is not None:

				queue.append(node.right)


if __name__ == '__main__':
	
	root = Node(1)

	root.left = Node(2)

	root.right = Node(3)

	root.left.left = Node(4)

	root.left.right = Node(5)

	print("Pre Order ")

	preorder(root)

	print()

	print("Post Order ")

	postorder(root)

	print()

	print("Inorder ")

	inorder(root)

	print()

	print("Breadth First Traversal ")

	bft(root)

	print()
