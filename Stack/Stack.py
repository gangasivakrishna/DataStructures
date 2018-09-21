#Stack
# push pop peer isEmpty

def createStack():

	stack = []

	return stack

def isEmpty(stack):

	return len(stack) == 0

def push(stack , data):

	stack.append(data)

	print(data ," pushed to stack")

def pop(stack):

	print(stack)

	if(isEmpty(stack)):

		return str(-maxsize - 1)

	return stack.pop()


def peek(stack):

	if(isEmpty(stack)):

		return str(-maxsize -1)

	return stack[len(stack)-1]


if __name__ == '__main__':

	stack = createStack()
	
	while True:
		
		print("1 Push 2 Pop 3 Peek or Top 4 isEmpty ")

		ch = int(input())

		if(ch == 1):

			data = input("Enter Data : ")

			push(stack,data)

		elif(ch == 2):

			print(pop(stack))

		elif(ch == 3):

			print(peek(stack))

		elif(ch == 4):

			print(isEmpty(stack))

		elif(ch ==5):

			print(stack)
