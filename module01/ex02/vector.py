
def	check_values(val):
	if type(val) != list:
		return print("Not a List")
	if not val:
		return print("Empty List")
	if (len(val) > 1 and len(val) < 3) or len(val) < 1:
		return print("Wrong List size")
	if len(val) == 1:
		for i in val:
			if not i:
				return print("Empty list")
			elif type(i[0]) != float:
				return print("Not a float")
			if type(i) != list:
				return print("Not a list")
	else:
		for i in val:
			if not i:
				return print("Empty list")
			elif type(i[0]) != float:
				return print("Not a float")
			if len(i) != 1:
				return print("Incorrect size of list")
			if type(i) != list:
				return print("Not a list")
	return 0

def	get_shape(values):
	if len(values) == 1:
		shape = (1, len(values[0]))
	else:
		shape = (len(values) , 1)
	return shape

def	instantiate(values):
	inst = Vector([[0., 0., 0.]])
	inst.values = values
	inst.shape = get_shape(inst.values)
	return inst

class Vector:
	def	__init__(self, values):
		if check_values(values) != 0:
			return print("ERRROR")
		self.values = values
		self.shape = get_shape(self.values)
	def	__str__(self):
		return "Vector(" + str(self.values) + ")"
	def	dot(self, vector):
		if not isinstance(vector, Vector):
			return print("Not class Vector")
		if self.shape != vector.shape:
			return print("Not the same shape")
		d = 0
		if len(self.values) == 1:
			for i in range(len(self.values[0])):
				d += self.values[0][i] * vector.values[0][i]
		else:
			for i in range(len(self.values)):
				d += self.values[i][0] * vector.values[i][0]
		return d
	def	T(self):
		new_vector=[]
		if len(self.values) == 1:
			for val in self.values[0]:
				new_vector.append([val])
			trans = instantiate(new_vector)
		else:
			for val in self.values:
				new_vector.append(val[0])
			trans = instantiate([new_vector])
		return trans
	def	__add__(self, vector):
		new_vector = []
		if len(self.values) == 1:
			for i in range(len(self.values[0])):
				new_vector.append(self.values[0][i]+vector.values[0][i])
			add_res = instantiate([new_vector])
		else:
			for i in range(len(self.values)):
				new_vector.append([self.values[i][0]+vector.values[i][0]])
			add_res = instantiate(new_vector)
		return add_res
	def	__sub__(self, vector):
		new_vector = []
		if len(self.values) == 1:
			for i in range(len(self.values[0])):
				new_vector.append(self.values[0][i]-vector.values[0][i])
			sub_res = instantiate([new_vector])
		else:
			for i in range(len(self.values)):
				new_vector.append([self.values[i][0]-vector.values[i][0]])
			sub_res = instantiate(new_vector)
		return sub_res
	def	__mul__(self, scalar):
		new_vector = []
		if len(self.values) == 1:
			for i in range(len(self.values[0])):
				new_vector.append(self.values[0][i]*scalar)
			mul_res = instantiate([new_vector])
		else:
			for i in range(len(self.values)):
				new_vector.append([self.values[i][0]*scalar])
			mul_res = instantiate(new_vector)
		return mul_res
	def	__truediv__(self, scalar):
		new_vector = []
		if len(self.values) == 1:
			for i in range(len(self.values[0])):
				new_vector.append(round(self.values[0][i]/scalar, 2))
			mul_res = instantiate([new_vector])
		else:
			for i in range(len(self.values)):
				new_vector.append([round(self.values[i][0]/scalar, 2)])
			mul_res = instantiate(new_vector)
		return mul_res