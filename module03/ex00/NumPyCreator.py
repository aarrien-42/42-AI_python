import numpy

def check(f):
	def final_function(self, x):
		if f.__name__ == "from_list" and type(x) != list:
				return None
		elif f.__name__ == "from_tuple" and type(x) != tuple:
			return None
		if f.__name__ == "from_list" and type(x[0]) == list \
			or f.__name__ == "from_tuple" and type(x[0]) == tuple:
			for i1 in x:
				if f.__name__ == "from_list" and type(i1) != list:
					return None
				elif f.__name__ == "from_tuple" and type(i1) != tuple:
					return None
				for i2 in x:
					if len(i1) != len(i2):
						return None
		try:
			return f(self, x)
		except:
			return None
	return final_function


class NumPyCreator:
	@check
	def from_list(self, lst):
		return numpy.array(lst)
	@check
	def from_tuple(self, tpl):
		return numpy.array(tpl)
	def from_iterable(self, itr):
		return numpy.fromiter(itr, int)
	def from_shape(self, shape, value=0):
		if type(shape) != tuple and len(shape) != 2:
			return None
		return numpy.full(shape, value)
	def random(self, shape):
		if type(shape) != tuple and len(shape) != 2:
			return None
		return numpy.random.rand(shape[0], shape[1])
	def identity(self, n):
		return numpy.identity(n)



if __name__ == '__main__':
	x = NumPyCreator()
	a = x.from_list([[1, 2, 3], [3, 2, 1], [2, 3, 1]])
	print(f"List:\n{a}\n")
	b = x.from_tuple((1, 2, 3))
	print(f"Tuple:\n{b}\n")
	c = x.from_iterable(range(5))
	print(f"Iterable:\n{c}\n")
	d = x.from_shape((2, 3), 2)
	print(f"Shape:\n{d}\n")
	e = x.random((2, 3))
	print(f"Random:\n{e}\n")
	f = x.identity(5)
	print(f"Identity:\n{f}\n")
