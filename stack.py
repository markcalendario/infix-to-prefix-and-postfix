class Node:
	# Node for the stack
	def __init__(self, element, next=None):
		self.element = element
		self.next = next

class Stack:
	# This stack uses linkedlist instead of array
	def __init__(self, headNode=None, tailNode=None):
		self.head = headNode
		self.tail = tailNode
	
	def push(self, element):
		# Pushes element to a stack
		node = Node(element)

		if self.head == None:
			self.head = node
		else:
			self.tail.next = node

		self.tail = node

	def pop(self):
		# Pops element to the stack
		if self.is_empty():
			return None

		popped_element = None

		# If the head is last
		if self.head.next == None:
			popped_element = self.head.element
			self.head = None
			self.tail = None
			return popped_element

		# If nodes count is not 1, iterate from head to node before tail
		current = self.head
		prev = None
		while current.next != None:
			prev = current
			current = current.next

		popped_element = current.element
		prev.next = None # unlink the prev to next
		self.tail = prev
		return popped_element

	def is_empty(self):
		# Checks if empty
		if self.head == None:
			return True
		return False

	def peek(self):
		# Returns the peek (last element inserted) from the stack
		if self.is_empty():
			return None
		return self.tail.element

	def display(self):
		# Displays all of the elements in the stack
		current = self.head
		while current != None:
			print(current.element, end='')
			current = current.next