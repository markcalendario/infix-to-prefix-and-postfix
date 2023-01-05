"""
Group 2:
	Borja, Czarina Khiara
	Cabildo, Picolo Jasper
	Calendario, Mark Kenneth
	Caritativo, Renz Carlo
	Rosales, Denelle Dione
	Ong, Zoe Tatianna
	Villas, Richter
"""

import os
from welcome_art import display_welcome_art
from infix_to_prefix import infix_to_prefix
from infix_to_postfix import infix_to_postfix
from menu import display_menu, getUserMenuInput

def start():
	display_menu()
	choice = getUserMenuInput()

	if choice == "A":
		os.system('cls')
		infix_to_postfix()
		start()
	elif choice == "B":
		os.system('cls')
		infix_to_prefix()
		start()
	elif choice == "X":
		os.system("cls")
		display_welcome_art()
		print("Exiting... Thank you!")
		os._exit(0)

os.system("cls")
display_welcome_art()
start()
