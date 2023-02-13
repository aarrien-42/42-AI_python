import datetime
from recipe import Recipe

def	input_check(n, rl):
	if type(n) != str or type(rl) != dict:
		return print("Book Type Error")
	if not n or not rl:
		return print("Book Empty Error")
	return 0

def	get_date():
	date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
	return date

class	Book:
	def	__str__(self):
		print(f"\nBook name: {self.name}")
		print(f"  -last_update = {self.last_update}")
		print(f"  -creation_date = {self.creation_date}")
		print(f"  -recipes_list:")
		print("    starter:", end="")
		for l in self.recipes_list['starter']:
			print(f"\n      -{l.name}" ,end="")
		print("\n    lunch:", end="")
		for l in self.recipes_list['lunch']:
			print(f"\n      -{l.name}" ,end="")
		print("\n    dessert:", end="")
		for l in self.recipes_list['dessert']:
			print(f"\n      -{l.name}" ,end="")
		return ""
	def	__init__(self, n, rl):
		if input_check(n, rl) != 0:
			return print ("Book Not created!")
		self.name = n
		self.last_update = get_date()
		self.creation_date = get_date()
		self.recipes_list = rl
	def	get_recipe_by_name(self, name):
		for k in self.recipes_list.keys():
			for v in self.recipes_list[k]:
				if v.name == name:
					print(v)
					return v
		print("Recipe not found")
	def	get_recipe_by_types(self, recipe_type):
		if recipe_type != "starter" and recipe_type != "lunch" and recipe_type != "dessert":
			return print("Type does not exist")
		print(f"Recipes for type {recipe_type}:")
		for re in self.recipes_list[recipe_type]:
			print(f"  -{re.name}")
	def	add_recipe(self, recipe):
		if not isinstance(recipe, Recipe) or not recipe.name:
			return print ("Not right class")
		print(f"Recipe {recipe.name} added succesfully")
		self.recipes_list[recipe.recipe_type].append(recipe)
		self.last_update = get_date()
