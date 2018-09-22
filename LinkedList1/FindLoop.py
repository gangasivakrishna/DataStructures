"""Floyd loop detection algorithm

	i=j=1

	i = i+1

	j = j+2

	if i == j:

		loop found

		break


Ex:  1 -> 2 -> 3 -> 4 -> 5 
               ^         |
               |         |
               ----------6

"""

class Node:

	def __init__(self,data):

		self.data = data

		self.next = None


class LinkedList:

	def __init__(self):

		self.head = None


	def detectLoop(self):

		fast = self.head

		slow = self.head

		while slow and fast and fast.next:
			
			slow = slow.next

			fast = fast.next.next

			if slow == fast:

				temp = fast

				print("Loop Found!!")

				break
		# print("temp: ",temp.data)

		dup = temp

		count = 0

		while(temp.next):

			count +=1

			if temp.next == dup:

				break

			else:

				temp = temp.next

		print("Length of the loop : ",count)



	def loopLength(self):

		pass




if __name__ == '__main__':
	
	ll = LinkedList()

	ll.head = Node(1)

	second = Node(2)

	third = Node(3)

	fourth = Node(4)

	fifth = Node(5)

	sixth = Node(6)

	seventh = Node(6)

	ll.head.next = second

	second.next = third

	third.next = fourth

	fourth.next = fifth

	fifth.next = sixth

	sixth.next = seventh

	seventh.next = third

	ll.detectLoop()