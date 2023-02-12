def	check_input(lst1, lst2):
	if type(lst1) != list or type(lst2) != list:
		return -1
	if len(lst1) != len(lst2):
		return -1
	return 0

class	Evaluator:
	def	zip_evaluate(coefs, words):
		if check_input(coefs, words) != 0:
			return -1
		res = list(zip(coefs, words))
		values = sum([coefs[i]*len(words[i]) for i in range(len(coefs))])
		return values
	def	enumerate_evaluate(coefs, words):
		if check_input(coefs, words) != 0:
			return -1
		res = list(enumerate(words))
		values = 0
		for num in res:
			values += coefs[num[0]] * len(words[num[0]])
		return values
		

coefs = [1.0, 2.0, 1.0, 4.0, 0.5]
words = ["Ñe", "Lorem", "Ipsum", "est", "simple"]
print(f"Zip = {Evaluator.zip_evaluate(coefs, words)}")
print(f"Enumerate = {Evaluator.enumerate_evaluate(coefs, words)}")
