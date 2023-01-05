from styles import displayStyledText, Colors
operators = ['+','*','-', '/']

def is_infix_expression_valid(expression):
	# This function checks if infix expression entered by the user is valid
	# And returns boolean

	if has_illegal_chars_in_expression(expression):
		displayStyledText(Colors.BG_RED, Colors.WHITE, "Invalid Infix", Colors.BG_WHITE, Colors.RED, "Illegal character found in the expression.")
		return False

	if has_operator_before_or_after_expression(expression):
		displayStyledText(Colors.BG_RED, Colors.WHITE, "Invalid Infix", Colors.BG_WHITE, Colors.RED, "Operator found before or after the expression.")
		return False

	if not has_balance_parenthesis(expression):
		displayStyledText(Colors.BG_RED, Colors.WHITE, "Invalid Infix", Colors.BG_WHITE, Colors.RED, "Uneven parenthesis in the expression.")
		return False

	if has_contiguous_operators(expression):
		displayStyledText(Colors.BG_RED, Colors.WHITE, "Invalid Infix", Colors.BG_WHITE, Colors.RED, "Contiguous operator found.")
		return False

	if not has_valid_expression_inside_parenthesis(expression):
		displayStyledText(Colors.BG_RED, Colors.WHITE, "Invalid Infix", Colors.BG_WHITE, Colors.RED, "Invalid expression inside the parenthesis.")
		return False

	return True

def has_valid_expression_inside_parenthesis(expression):
	# This function checks the ff:
	# 1. An operator after open parenthesis
	# 2. An operator before close parenthesis
	# 3. An empty expression inside the open and close parenthesis

	# Check empty expression inside parenthesis
	is_previous_char_open_parenthesis = False

	for i in expression:
		if i == ')' and is_previous_char_open_parenthesis:
			return False
		
		if i == '(':
			is_previous_char_open_parenthesis = True
		else:
			is_previous_char_open_parenthesis = False

	# Check if a char is operator after open parenthesis
	is_previous_char_open_parenthesis = False

	for i in expression:
		if i in operators and is_previous_char_open_parenthesis:
			return False

		if i == '(':
			is_previous_char_open_parenthesis = True
		else:
			is_previous_char_open_parenthesis = False

	# Check if a char is operator before close parenthesis
	is_previous_char_operator = False

	for i in expression:
		if i == ')' and is_previous_char_operator:
			return False

		if i in operators:
			is_previous_char_operator = True
		else:
			is_previous_char_operator = False

	return True

def has_operator_before_or_after_expression(expression):
	# Check if there are operators before or after the expression
	# Return true if found
	first_char = expression[0]
	last_char = expression[len(expression) - 1]
	if first_char in operators or last_char in operators:
		return True

	return False

def has_illegal_chars_in_expression(expression):
	# Check illegal expressions
	# Return true if found
	legal_chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789+-*/()'

	for i in list(expression):
		if i.upper() not in legal_chars:
			return True

	return False

def has_balance_parenthesis(expression):
	# Check parenthesis if balance
	# Return false if found uneven

	# Remove all characters except open and close parenthesis
	exp_test = expression
	for i in exp_test:
		if i != '(' and i != ')':
			exp_test = exp_test.replace(i, '')
	
	# If count of parenthesis is not even
	if not len(exp_test) % 2 == 0:
		return False

	# Check if parentheses have partners
	# Return false if do not have
	parenthesisStack = []

	for i in exp_test:
		if i == '(':
			parenthesisStack.append(i)

		elif len(parenthesisStack) == 0:
				return False

		elif not parenthesisStack.pop() == '(':
				return False

	# If there are parentheses left in the stack,
	# return false
	if len(parenthesisStack) != 0:
		return False

	return True

def has_contiguous_operators(expression):
	# Check if there is operator after operator
	# Return true if there is
	is_prev_token_operator = False

	for i in expression:
		if i in operators and is_prev_token_operator:
			return True
		
		if i in operators:
			is_prev_token_operator = True
		else:
			is_prev_token_operator = False
	
	return False