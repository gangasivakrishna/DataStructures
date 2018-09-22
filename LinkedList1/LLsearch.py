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


	def iterativeSearch(self,key):

		temp = self.head

		while(temp):

			if temp.data == key :

				return True

			temp = temp.next

		return False


	def recursiveSearch(self,li,key):

		if not li:

			return False

		if li.data == key:

			return True

		else:

			return self.recursiveSearch(li.next,key)




	def display(self):

		if self.head is None:

			print("LinkedList empty!!")

		else:

			temp = self.head

			while(temp):

				print(temp.data,end='->')

				temp = temp.next

			print('Null')


if __name__ == '__main__':
	



	ll = LinkedList()

	while True:

		print("1 Add 2 Iterative Key Search 3 Recursive Key Search 4 Display ")

		ch = int(input())

		if ch == 1:

			data = input("Enter Data : ")

			ll.append(data)

		elif ch == 2:

			key = input("Enter key to search : ")

			status = ll.iterativeSearch(key)

			if status:

				print("Key found!!")

			else:

				print("Key not found!!")

		elif ch == 3:

			key = input("Enter key to search : ")

			status = ll.recursiveSearch(ll.head,key)

			if status:

				print("Key found!!")

			else:

				print("Key not found!!")

		elif ch == 4 :

			ll.display()

		else:

			sys.exit(0)




