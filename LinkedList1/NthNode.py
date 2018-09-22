"""
Problem : Single Linked List

Descritpin: Single LinkedList Operations

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

	def nthnode(self,node,n,count):

		if node is None:

			return

		elif count == n:

			return node.data

		else:

			return self.nthnode(node.next,n,count+1)


	def findLast(self,n):

		length = self.findLength(self.head)


		temp  = self.head

		count = 0

		while(temp):

			if count == length-n-1:

				print(temp.data)

				break

			else:

				count+=1

				temp = temp.next




		# if node is None:

		# 	return

		# elif count == length:

		# 	return node.data

		# else:

		# 	return self.findLast(node.next,length,count+1)



	def findLength(self,node):

		if node is None:

			return 0

		else:

			return 1+ self.findLength(node.next)


	def findMiddle(self):

		length = self.findLength(self.head) -1


		mid = length>>1

		temp = self.head

		count = 0

		while(temp):

			if count == mid:

				print(temp.data)

				break

			else:

				temp = temp.next

				count+=1



	def display(self,node):

		if node is None:

			print("Null")

		else:

			print(node.data,end='->')

			self.display(node.next)



if __name__ == '__main__':
	
	ll =  LinkedList()

	while True:
		
		print("1 Append 2 Nth node 3 Nth node from End 4 Middle 5 Display ")

		ch = int(input())

		if ch == 1:

			data = input("Enter data : ")

			ll.append(data)

		elif ch == 2:

			n = int(input("Enter N :"))

			print("Nth node: ",ll.nthnode(ll.head,n,0))

			# print("N th node is ",nth)

		elif ch == 3:

			n = int(input("Enter N for last : "))

			print("Nth node from reverse order : ",ll.findLast(n))

		elif ch == 4:

			print("Middle Element is : ",end = ' ')
			
			ll.findMiddle()

		elif ch == 5:

			ll.display(ll.head)





