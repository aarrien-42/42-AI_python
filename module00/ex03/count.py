import sys

def	text_analyzer(text=None):
	'''\nThis function counts the number of upper characters, lower characters, punctuation and spaces in a given text.\n'''
	if text == None:
		text = input("What is the text to analyze?\n>> ")
	if type(text) != list and type(text) != str:
		return print("AssertionError: argument is not a string")
	if type(text) == list:
		if len(text) > 1:
			return print("AssertionError: too many arguments supplied")
		else:
			text = text[0]
	low = up = spaces = p = c = 0
	for i in text:
		if i == ' ':
			spaces += 1
		if i.islower() == True:
			low += 1
		if i.isupper() == True:
			up += 1
		if i >= '!' and i <= '/':
			p += 1
		c += 1
	print(f"The text contains {c} character(s):")
	print(f"- {up} upper letter(s)")
	print(f"- {low} lower letter(s)")
	print(f"- {p} punctuation mark(s)")
	print(f"- {spaces} space(s)")

if __name__ == "__main__":
	if len(sys.argv) < 2:
		text = ""
		while len(text) == 0:
			text = input("What is the text to analyze?\n>> ")
		text_analyzer(text)
	text_analyzer(sys.argv[1:])

"Python 2.0, released 2000, introduced features like List comprehensions and a garbage collection system capable of collecting reference cycles."

"Python is an interpreted, high-level, general-purpose programming language. Created by Guido van Rossum and first released in 1991, Python's design philosophy emphasizes code readability with its notable use of significant whitespace."
