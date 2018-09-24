class Node :

	def __init__(self,data):

		self.data = data

		self.next = None

		self.pre = None


class DoubleList:

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

			new_node.pre = temp

	def display(self):

		if self.head is None:

			print("Empty")

		else:

			temp = self.head

			while(temp):

				print(temp.data,end = '->')

				temp = temp.next

			print('Null')


if __name__ == '__main__':
	
	dl = DoubleList()

	inp = list(map(int,input().split()))

	for i in inp:

		dl.append(i)

	dl.display()