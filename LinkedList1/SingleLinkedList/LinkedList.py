"""
Problem : Single Linked List

Descritpin: Single LinkedList Implementation

Author : Siva Krishna

Date : 21-09-2018

"""


#LinkedList Node Creation

"""Linked list node has two fields  one is data and another one is next

next is ponted to the next node,initially it is None"""

class Node:

	def __init__(self,data):

		self.data = data

		self.next = None


#LinkedList Class

"""Linked list has head,it is a very first node and Last Node's next refer to Null"""

class LinkedList:

	def __init__(self):

		self.head = None



if __name__ == '__main__':
	
	ll = LinkedList()

	ll.head = Node(1)

	second = Node(2)

	third = Node(3)

	ll.head.next = second

	second.next = third