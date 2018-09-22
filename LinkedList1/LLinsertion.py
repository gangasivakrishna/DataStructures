
import sys

#LinkedList Insertion operations

class Node:

	def __init__(self,data):

		self.data = data

		self.next = None


class LinkedList:

	def __init__(self):

		self.head = None

		#adding elements to the linked list

	# 1. Create a Node
	# 2. Check whether head is empty,if empty assign created Node to head
	# 3. if not,assign head to temp variable and traverse to last node and point last node next to the created Node

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

	#Insertion

	def insertBefore(self,key,data):

		#Node creation
		flag = False

		new_node = Node(data)

		if self.head is None:

			print("Linkedlist empty!!")

		elif self.head.data == key:

			new_node.next = self.head

			self.head = new_node

			return True

		else:

			temp = self.head

			while(temp.next):

				if temp.next.data == key:

					new_node.next = temp.next

					temp.next = new_node

					flag = True

					return flag

				temp = temp.next

			return flag



	def insertAfter(self,key,data):

		flag = False

		new_node = Node(data)

		if self.head is None:

			print("LinkedList empty!!")


		else:

			temp = self.head

			while (temp):
				
				if temp.data == key:

					new_node.next = temp.next

					temp.next = new_node

					flag = True

					return flag

				temp = temp.next

			return flag

	# Display Linkedlist items

	def traversal(self):

		if self.head is None:

			print("No items in the LinkedList")

		else:

			temp = self.head

			while(temp):

				print(temp.data,end = '->')

				temp = temp.next

			print('Null')
				





if __name__ == '__main__':
	

	#LinkedList object instance creation

	ll = LinkedList()
	
	while True:

		print()
		
		print("1 Inesrt at End 2 InsertBefore 3 InsertAfter 4 Display")

		print()

		ch = int(input())

		if(ch == 1):

			data = input("Enter data : ")

			ll.append(data)

		elif(ch == 2):

			key = input("Enter Key : ")

			data = input("Enter data : ")

			insertState = ll.insertBefore(key,data)

			if insertState:

				print("Inserted before the ",key)

			else:

				print("insertion failed!!")

		elif(ch == 3):

			key = input("Enter Key : ")

			data = input("Enter data : ")

			insertState = ll.insertAfter(key,data)

			if insertState:

				print("Inserted after the ",key)

			else:

				print("insertion failed!!")

		elif(ch == 4):

			print()

			ll.traversal()

		else:

			sys.exit(0)
