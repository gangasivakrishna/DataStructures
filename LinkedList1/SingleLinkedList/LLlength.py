"""
Problem : Single Linked List

Descritpin: Single LinkedList Operations

Author : Siva Krishna

Date : 21-09-2018

"""


#LinkedList Node Creation

"""Linked list node has two fields  one is data and another one is next

next is ponted to the next node,initially it is None"""

import sys

class Node:

	def __init__(self,data):

		self.data = data

		self.next = None


class LinkedList:

	def __init__(self):

		self.head = None


	def append(self,data):

		new_node = Node(data)

		if self.head is None:

			self.head = new_node

		else:

			temp = self.head

			while(temp.next):

				temp = temp.next

			temp.next = new_node


	def iterativeLength(self):

		count = 0

		temp = self.head

		while temp:
			
			count += 1

			temp = temp.next

		print("Length of the LinkedList : ",count)


	def getLength(self,node):

		if node is None:

			return 0

		else:

			return 1+ self.getLength(node.next)

	def recursiveLength(self):

		print("Length of LinkedList : ",self.getLength(self.head))



	def display(self):

		if self.head is None:

			print("LinkedList empty !!")

		else:

			temp = self.head

			while(temp):

				print(temp.data,end='->')

				temp = temp.next

			print('Null')





if __name__ == '__main__':
	

	ll = LinkedList()

	while True:

		print("1 Add 2 Iterative length 3 Recursive length 4 Display ")

		ch = int(input())

		if ch == 1:

			data = input("Enter Data : ")

			ll.append(data)

		elif ch == 2:

			ll.iterativeLength()

		elif ch == 3:

			ll.recursiveLength()

		elif ch == 4 :

			ll.display()

		else:

			sys.exit(0)

