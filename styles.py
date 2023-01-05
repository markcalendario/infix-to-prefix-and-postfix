def separator(): 
	print("===================================================")

class Colors:
	BLACK = "\033[1;30m"
	RED = "\033[1;91m"
	BG_RED = "\033[1;101m"
	GREEN = "\033[1;92m"
	BG_GREEN = "\033[1;102m"
	YELLOW = "\033[1;93m"
	BLUE = "\033[1;94m"
	WHITE= "\033[1;97m"
	BG_WHITE = "\033[1;107m"
	BOLD = "\033[1m"
	ITALIC = "\033[3m"
	UNDERLINE = "\033[4m"
	BLINK = "\033[5m"
	END = "\033[0m"

def displayStyledText(titleBG, titleFG, title, textBG, textFG, text):
	print(titleBG + titleFG + " " + title + " " + textBG + textFG + " " + text + " " + Colors.END)