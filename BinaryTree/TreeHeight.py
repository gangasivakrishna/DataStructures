#Tree Node

class Node :

	def __init__(self,key):

		self.left = None

		self.right = None

		self.val = key

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



"""
	          1
	    	/   \
	       /     \
	      2       3
	     / \
	    /   \
	   4     5

"""