class	GotCharacter:
	def	__init__(self, fn, ia):
		self.first_name = fn
		self.is_alive = ia
	first_name=""
	is_alive=True
class	Stark(GotCharacter):
	"""A class representing the Stark family. Or when bad things happen to good people."""
	def	__init__(self, first_name=None, is_alive=True):
		super().__init__(first_name, is_alive)
		self.family_name="Stark"
		self.house_words="Winter is Coming"
	def	print_house_words(self):
		print(self.house_words)
	def	die(self):
		self.is_alive = False

if __name__ == '__main__':
	arya = Stark("Arya")
	arya.print_house_words()
	print(arya.is_alive)
	arya.die()
	print(arya.is_alive)
	print(dict(arya.__dict__))
	print(arya.__doc__)