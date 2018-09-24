

class Node:

	def __init__(self,data):

		self.data = data

		self.next = None



class CircularList:

	def __init__(self):

		self.head = None


	def append(self,data):

		new_node = Node(data)

		new_node.next = self.head

		if self.head is None:

			self.head = new_node

			new_node.next = self.head

		else:

			temp = self.head

			while(temp.next is not self.head):

				temp = temp.next

			temp.next = new_node

	def splitList(self):

		slow_ptr = self.head

		fast_ptr = self.head

		while(fast_ptr.next != self.head and fast_ptr.next.next != self.head):

			fast_ptr = fast_ptr.next.next

			slow_ptr = slow_ptr.next

		print(fast_ptr.data)
		print(slow_ptr.data)
	def display(self):

		if self.head is None:

			print("List empty !!")

		else:

			temp = self.head

			while temp.next is not self.head:

				print(temp.data,end = '->')

				temp = temp.next

			print(temp.data,end ='->')
			print(temp.next.data)
				

if __name__ == '__main__':
	
	cl = CircularList()

	while True:
		
		print(" 1 Append 2 Remove 3 Insert 4 Display")

		ch = int(input())

		if ch == 1:

			data = input("Eneter data : ")

			cl.append(data)

		elif ch == 2:

			cl.splitList()

		elif ch == 3:

			pass

		elif ch == 4:

			cl.display()