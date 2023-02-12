import random

def shuffle(text):
	for i in range(len(text)-1, 0, -1):
		j = random.randint(0, i)
		text[i], text[j] = text[j], text[i]
	return text

def	generator(text, sep=" ", option=None):
	'''Splits the text accordiong to sep values and yield the substrings.'''
	if type(text) != str:
		return print("ERROR")
	if option != "shuffle" and option != "ordered" and option != "unique" and option != None:
		return print("ERROR")
	text = text.split(sep)
	if option == "shuffle":
		text = shuffle(text)
	elif option == "ordered":
		text = sorted(text)
	elif option == "unique":
		text = list(dict.fromkeys(text))
	for word in text:
		yield word

for word in generator("Lorem Ipsum Lorem Ipsum", " "):
	print(word)