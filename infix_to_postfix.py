from styles import displayStyledText, Colors
from stack import Stack
from infix_expression_validator import is_infix_expression_valid

def infix_to_postfix():
	# Get infix expression from the user
	expression = ''

	# Loop if user entered invalid infix expression
	while True:
		expression = input("Please type a valid infix expression: ")
		if is_infix_expression_valid(expression):
			break
		else:
			print("")
	
	# Start
	output = convert_to_postfix(expression)
	displayStyledText(Colors.BG_GREEN, Colors.WHITE, "POSTFIX", Colors.BG_WHITE, Colors.GREEN, "".join(output))

def convert_to_postfix(expression):

	operator_stack = Stack()
	output_stack = []
	operators = ['+','*','-', '/', '(', ')']

	# Read all the tokens in the expression
	for i in expression:
		# If token is not operator
		if not i in operators:
			# Push to the output stack
			output_stack.append(i)
		
		# If token is operator and operator stack is empty
		elif i in operators and operator_stack.is_empty():
			# Push to the operator stack
			operator_stack.push(i)

		# If token is * and /
		elif i == '*' or i == '/':
			# Pop and push all of the token with highest and same priority 
			# from the operator stack to the output stack
			while True:
				if operator_stack.peek() == '*' or operator_stack.peek() == '/':
					output_stack.append(operator_stack.pop())
				else:
					break
			# Then push the current token to the operator stack
			operator_stack.push(i)	

		# If token is + and -
		elif i == '+' or i == '-':
			# Pop and push all of the token with highest and same priority 
			# from the operator stack to the output stack
			while True:
				peek = operator_stack.peek()
				if peek == '*' or peek == '/' or peek == '+' or peek == '-':
					output_stack.append(operator_stack.pop())
				else:
					break
			# Then push the current token to the operator stack
			operator_stack.push(i)

		# If token is (
		elif i == '(':
			# Push to the operator stack
			operator_stack.push(i)

		# If stack is )
		elif i == ')':
			# Pop all of the entries in the operator stack until reaching (
			while True:
				peek = operator_stack.peek()
				if peek == '(':
					operator_stack.pop()
					break
				else:
					output_stack.append(operator_stack.pop())

	# Transfer all of the tokens left from the operator stack
	# to the output stack
	while True:
		if operator_stack.peek() == None:
			break
		else:
			output_stack.append(operator_stack.pop())

	# Return the output stack
	return "".join(output_stack)
