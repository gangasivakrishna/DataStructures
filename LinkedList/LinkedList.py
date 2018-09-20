#Node class

class Node:

	#Node objects initialization

	def __init__(self,data):

		self.data = data

		self.next = None


#LinkedList Class

class LinkedList:

	def __init__(self):

		self.head = None

	#Add elements to the linked list

	def append(self,data):

		#New Node creation

		new_node = Node(data)

		if self.head == None:

			self.head = new_node

		else:

			temp = self.head

			while(temp.next):

				temp = temp.next

			temp.next = new_node


	#LinkedList Delete

	def delete(self,key):


		if self.head.data == key:

			self.head = self.head.next

		else:

			temp = self.head

			while(temp.next):

				if(temp.next.data == key):

					temp.next = temp.next.next

					return True

				temp = temp.next

			return False


	#LinkedList Insert

	def insert(self,key,data):

		new_node = Node(data)

		if self.head is None:

			self.head = new_node


		elif self.head.data == key :

			new_node.next = self.head.next

			self.head.next = new_node

		else:

			temp = self.head.next

			while(temp.next):
				
				if(temp.data == key):

					new_node.next = temp.next

					temp.next = new_node

					return True

				temp = temp.next

			return False

	#LinkedList Rotate

	def rotate(self,length):

		count = 0

		temp = self.head

		new_head = self.head

		while(temp):

			count+=1

			if(count == length):

				new_temp = temp.next

				break

			temp = temp.next


		prev = temp

		present = new_temp

		self.head = present

		prev.next = None

		while (present.next):
			
			# print(present.data)

			present = present.next

		present.next = new_head

	#delete all nodes

	def deleteall(self):

		self.head = None


	#reverse linked list

	def reverse(self):

		if self.head is None:

			print("No item in the linked list")

		else:

			prev = None

			cur = self.head


			while(cur):

				next = cur.next

				cur.next = prev

				prev = cur

				cur = next				

			self.head = prev


	# swap linkedlist

	#1->2->3->4->Null

	#2->1->4->3->Null


	def swaplist(self):

		temp = self.head

		nex = self.head.next

		while(temp.next):

			temp.data,nex.data = nex.data,temp.data

			temp = nex.next

			nex = temp.next

	def duplicates(self):

		dup_list = []

		dup_list.append(self.head.data)

		temp = self.head

		while(temp.next):

			if temp.next.data in dup_list:

				temp.next = temp.next.next

				if temp.next is not None:

					temp = temp.next

			else:

				dup_list.append(temp.next.data)

				temp = temp.next

		# print(exist_list)



	#LinkedList Traversal

	def display(self):

		temp = self.head

		while(temp):

			print(temp.data,end='->')

			temp = temp.next

		print("Null")





#code starts here

if __name__ == '__main__':

	#linkedlist object creation

	ll = LinkedList()

	while True:
		
		# input choice from user

		print("Enter 1 Add 2 Insert 3 Delete 4 Display  5 Rotate 6 DeleteAll 7 Reverse 8 SwapList 9 Remove Duplicates")


		ch = int(input("Enter choice : "))

		if(ch == 1):

			data = input("Enter Data : ")

			ll.append(data)

		elif(ch == 2):

			data = input("Enter data : ")

			key = input("Enter Key : ")

			value = ll.insert(key,data)

			if not value :

				print("Key not found !!")

		elif(ch == 3):

			key = input("Enter key : ")

			value = ll.delete(key)

			if not value :

				print("Key not found !!")


		elif(ch == 4):

			ll.display()

		elif(ch == 5):

			length = int(input("Enter length to Rotate : "))

			ll.rotate(length)

		elif(ch == 6):

			ll.deleteall()

		elif(ch == 7):

			ll.reverse()

		elif(ch == 8):

			ll.swaplist()

		elif(ch == 9):

			ll.duplicates()