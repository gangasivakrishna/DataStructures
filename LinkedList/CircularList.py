#Node Creation

class Node:

	def __init__(self,data):

		self.next = None

		self.data = data

#Circular List Class

class CircularList:

	def __init__(self):

		self.head = None

	#appending data

	def append(self,data):

		new_node = Node(data)

		new_node.next = self.head

		temp = self.head

		if self.head is not None:

			while(temp.next != self.head):

				temp = temp.next

			temp.next = new_node

		else:

			new_node.next = new_node

		self.head = new_node

	#linkedlist traversal
	
	def traversal(self):

		temp = self.head 

		if self.head is not None:

			while True:

				print(temp.data,end='->')

				temp = temp.next

				if(temp == self.head):

					break



if __name__ == '__main__':

	cl = CircularList()

	while True:

		print("1 Append 2 Display")

		ch = int(input())

		if(ch ==1):

			data = input("Enter data : ")

			cl.append(data)

		elif(ch == 2):

			cl.traversal()