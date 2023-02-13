def	input_check(n, cl, ct, ing, des, rt):
	if type(n) != str or type(cl) != int or type(ct) != int or type(ing) != list or type(des) != str or type(rt) != str:
		return print("Type Error")
	if not n or not ing or not ct or not cl:
		return print("Empty Error")
	if cl < 1 or cl > 5:
		return print("Cl Range Error")
	if ct < 0:
		return print("Negative Ct Error")
	if rt != "starter" and rt != "lunch" and rt !="dessert":
		return print ("Rt Error")
	return 0

class	Recipe:
	def	__str__(self):
		txt = \
		f"\nRecipe name: {self.name}\n" + \
		f"  -cooking_lvl = {self.cooking_lvl}\n" +\
		f"  -cooking_time = {self.cooking_time}min\n" +\
		f"  -ingredients = {self.ingredients}\n" +\
		f"  -description = {self.description}\n" +\
		f"  -recipe_type = {self.recipe_type}\n"
		return txt
	def	__init__(self, n, cl, ct, ing, des, rt):
		if input_check(n, cl, ct, ing, des, rt) != 0:
			return print ("Recipe Not created!")
		self.name = n
		self.cooking_lvl = cl
		self.cooking_time = ct
		self.ingredients = ing
		self.description = des
		self.recipe_type = rt
	name = ""