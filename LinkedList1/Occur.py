
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

	def count(self,node,m):

		if node is None:

			return 0

		if node.data == m:

			return 1+self.count(node.next,m)

		else:

			return self.count(node.next,m)


	def display(self):

		if self.head is None:

			print("Empty List")

		else:

			temp = self.head

			while (temp):
				
				print(temp.data,end = '->')

				temp = temp.next

			print('Null')

if __name__ == '__main__':

	test = int(input("Enter no.of test cases: "))

	while(test):

		ll = LinkedList()


		#input example  1 2 3 4 5

		inp = list(map(int,input().split()))

		for i in inp:

			ll.append(i)

		ll.display()

		m = int(input("Enter key : "))

		print(m,"appears ",ll.count(ll.head,m)," times")

		test -=1



	