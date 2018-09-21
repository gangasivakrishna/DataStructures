#Double Linked List

class Node:

	def __init__(self,data):

		self.next = None

		self.prev = None

		self.data = data



class DoubleList:

	def __init__(self):

		self.head = None

	def append(self,data):

		new_node = Node(data)

		temp = self.head

		if self.head is None :

			self.head = new_node

		else:

			while(temp.next):

				temp = temp.next

			new_node.prev = temp

			temp.next = new_node


	def display(self):

		temp = self.head

		if self.head is None:

			print("No items in the list ")

		else:

			while(temp):

				print(temp.data,end = '->')

				# print("temp prev data ",temp.prev)

				temp = temp.next

			print('Null')



if __name__ == '__main__':
	
	dl = DoubleList()

	while True:

		print("Enter 1 Append 2 Display")

		ch = int(input())

		if(ch == 1):

			data = input("Enter data : ")

			dl.append(data)

		elif(ch == 2):

			dl.display()