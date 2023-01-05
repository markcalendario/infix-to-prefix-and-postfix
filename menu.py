from styles import separator, Colors, displayStyledText

menu_keys_and_text = {
	"A": "Infix to Postfix",
	"B": "Infix to Prefix",
	"X": "Close"
}

def display_menu():
	# Displays menu from the menu_keys_and_text dictionary
	keys = menu_keys_and_text.keys()

	separator()
	print("Menu")	

	for i in keys:
		print("[" + i + "] " + menu_keys_and_text[i])
	
	separator()

def getUserMenuInput():
	# Get user menu input, only accepts 'A', 'B', and 'X'
	# Display error if not a valid choice
	while True:
		userInput = input("Your choice: ").upper()

		if userInput in menu_keys_and_text.keys():
			return userInput
		
		displayStyledText(Colors.BG_RED, Colors.WHITE, "Invalid Input", Colors.BG_WHITE, Colors.RED, f'{userInput} is not a valid choice.')

	