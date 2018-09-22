
import sys

class Node:

	def __init__(self,data):

		self.data = data

		self.next = None


class LinkedList:

	def __init__(self):

		self.head = None


	def append(self,data):

		#create a Node

		new_node = Node(data)

		if self.head is None:

			self.head = new_node

		else:

			temp = self.head

			while(temp.next):

				temp = temp.next

			temp.next = new_node

	def delLastNode(self):

		if self.head is None:

			print("LinkedList Empty!!")

		else:

			temp = self.head

			while(temp.next.next):

				temp = temp.next

			temp.next = temp.next.next

	def delete(self,key):

		flag = False

		temp = self.head

		if self.head is None:

			print("LinkedList empty!!")

		elif self.head.data == key:

			self.head = temp.next

			return True

		else:

			while(temp.next):

				if temp.next.data == key:

					temp.next = temp.next.next

					flag = True

					return flag

				temp = temp.next

			return flag

	#delete using index			
	def deleteIndex(self,index):

		flag = False

		count = 0

		temp = self.head

		if self.head is None:

			print("LinkedList empty!!")

		elif count == index:

			self.head = temp.next

			return True

		else:

			while(temp.next):

				count += 1

				if count == int(index):

					temp.next = temp.next.next

					flag = True

					return flag

				temp = temp.next

			return flag


	def deleteLinkedList(self):

		current = self.head

		while(current):

			prev = current.next

			del current.data

			current = prev


			# print("temp.data ",temp.data)

	# Display Linkedlist items

	def traversal(self):

		if self.head is None:

			print("No items in the LinkedList")

		else:

			try:
				temp = self.head

				while(temp):

					print(temp.data,end = '->')

					temp = temp.next

				print('Null')
				
			except AttributeError as e:

				print("LinkedList may be empty or error in Node Class !!")
			


if __name__ == '__main__':

	#LinkedList object instance creation

	ll = LinkedList()
	
	while True:

		print()
		
		print("1 Append 2 Delete Last Node 3 Delete Key Node 4 Delete Index Node 5 DeleteLinkedlist  6  Display")

		print()

		ch = int(input())

		if(ch == 1):

			data = input("Enter data : ")

			ll.append(data)

		elif(ch == 2):

			ll.delLastNode()

		elif (ch == 3):

			key = input("Enter Node to Delete : ")

			deleteStatus = ll.delete(key)

			if deleteStatus:

				print("Node deleted !!")

			else:

				print("Node deletion failed!!")
		elif (ch == 4):

			index = input("Enter Index to Delete( 0 to n) : ")

			deleteStatus = ll.deleteIndex(index)

			if deleteStatus:

				print("Node deleted !!")

			else:

				print("Node deletion failed!!")


		elif(ch == 5):

			ll.deleteLinkedList()


		elif(ch == 6):

			print()

			ll.traversal()

		else:

			sys.exit(0)

