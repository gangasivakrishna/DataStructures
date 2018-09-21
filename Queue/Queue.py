#Queue class

import sys

class Queue:
	"""docstring for Queue"""
	def __init__(self, capacity):
		
		self.front = self.size = 0

		self.rear = capacity-1

		self.Q = [None]*capacity

		self.capacity = capacity

	def isFull(self):

		return self.size == self.capacity

	def isEmpty(self):

		return self.size == 0

	def enque(self,element):

		if self.isFull():

			print("Q is Full ")

		else:

			self.rear = (self.rear +1) % (self.capacity)

			self.Q[self.rear] = element

			self.size += 1

	def deque(self):

		if self.isEmpty():

			print("Q is Empty ")

		else:

			print(self.Q[self.front], "Dequeud")

			self.front = (self.front+1)%(self.capacity)

			self.size -=1

	def frontItem(self):

		if self.isEmpty():

			print("Q is Empty")

		else:

			print("Front Item : ",self.Q[self.front])

	def rearItem(self):

		if self.isEmpty():

			print("Q is Empty ")

		else:

			print("Rear Item : ",self.Q[self.rear])

	def queue(self):

		print(self.Q)

#main function

if __name__ == '__main__':
	
	capacity  = int(input("Enter Capacity of Queue : "))

	Q = Queue(capacity)

	while True:

		print(" 1 Enque 2 Deque 3 Front Item 4 Rear Item 5 Display")

		ch = int(input())

		if ch == 1:

			data = input("Enter item : ")

			Q.enque(data)

		elif ch ==2:

			Q.deque()

		elif ch == 3:

			Q.frontItem()

		elif ch == 4:

			Q.rearItem()

		elif ch == 5:

			Q.queue()

		else:

			sys.exit(0)