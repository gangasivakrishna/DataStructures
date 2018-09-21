#Tree Node

class Node :

	def __init__(self,key):

		self.left = None

		self.right = None

		self.val = key


def printLevelOrder(node):

	h = height(node)

	for i in range(1,h+1):

		getLevelValues(node,i)

def getLevelValues(node,level):

	if node is None:

		return

	if level == 1:

		print(node.val,end = ' ')

	else:

		getLevelValues(node.left,level-1)

		getLevelValues(node.right,level-1)


#height calculation

def height(node): 
    
    if node is None:

    	return 0

    else:

    	left_height = height(node.left)

    	right_height = height(node.right)

    	if left_height > right_height:

    		return left_height+1

    	else:

    		return right_height+1




if __name__ == '__main__':
	
	root = Node(1)

	root.left = Node(2)

	root.right = Node(3)

	root.left.left = Node(4)

	root.left.right = Node(5)

	print("Height of the Tree : ",height(root))

	print("Level order : ",end = ' ')

	printLevelOrder(root)

	print()
	



print("""
	          1
	    	/   \
	       /     \
	      2       3
	     / \
	    /   \
	   4     5

""")