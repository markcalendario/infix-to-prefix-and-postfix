from styles import displayStyledText, Colors
from stack import Stack
from infix_expression_validator import is_infix_expression_valid
from infix_to_postfix import convert_to_postfix

def infix_to_prefix():
	# This function converts infix to prefix
	# Logic: 
	# Reverse the infix expression backwards
	# Replace all '(' to ')' and ')' to '('
	# Then, convert reversed expression to postfix
	# Lastly, bring back the reversed expression to normal form
	expression = ''

	while True:
		expression = input("Please type a valid infix expression: ")
		if is_infix_expression_valid(expression):
			break
		else:
			print("")

	expression = expression[::-1] # reverse the expression backwards
	expression = expression.replace('(', '%') # temporarily change '(' to '%'
	expression = expression.replace(')', '(')
	expression = expression.replace('%', ')')

	output = convert_to_postfix(expression)
	displayStyledText(Colors.BG_GREEN, Colors.WHITE, "PREFIX", Colors.BG_WHITE, Colors.GREEN, output[::-1])
