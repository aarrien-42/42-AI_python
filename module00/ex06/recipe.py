cookbook =	{"Sandwich":{"ing":"ham, bread, cheese, tomatoes", "meal":"lunch", "time":10},
			"Cake":{"ing":"flour, sugar, eggs", "meal":"dessert", "time":60},
			"Salad":{"ing":"avocado, arugula, tomatoes, spinach", "meal":"lunch", "time":15}}

def print_names():
	for name in cookbook.keys():
		print(name)

def print_details():
	name = input("Please enter a recipe name to get its details:\n>> ")
	if cookbook.get(name) == None:
		return (print("Sorry, this option does not exist."))
	print(f"\nRecipe for {name}")
	print(f"	Ingredients list: {cookbook[name]['ing']}")
	print(f"	To be eaten for {cookbook[name]['meal']}.")
	print(f"	Take {cookbook[name]['time']} minutes of cooking.\n")

def delete_recipe():
	name = input("Enter the recipe you want to delete:\n>> ")
	if cookbook.get(name) == None:
		return (print("Sorry, this option does not exist."))
	del cookbook[name]

def add_recipe():
	name = input(">>> Enter a name:\n")
	print(">>> Enter the ingredients:")
	ing = []
	while True:
		ingredient = input("")
		if ingredient == "":
			break
		ing.append(ingredient)
	meal = input(">>> Enter a meal type:\n")
	time = input(">>> Enter a preparation time:\n")
	cookbook[name] = {"ing":ing, "meal":meal, "time":time}

def show_options():
	print("List of available option:")
	print("	1: Add a recipe")
	print("	2: Delete a recipe")
	print("	3: Print a recipe")
	print("	4: Print the cookbook")
	print("	5: Quit\n")

def selection():
	option = input("Please select an option:\n>> ")
	if option.isnumeric() == False or int(option) > 5 or int(option) <= 0:
		print("Sorry, this option does not exist.")
		show_options()
	elif int(option) == 1:
		add_recipe()
	elif int(option) == 2:
		delete_recipe()
	elif int(option) == 3:
		print_details()
	elif int(option) == 4:
		print_names()
	elif int(option) == 5:
		exit(print("\nCookbook closed. Goodbye !"))
	selection()

def main():
	print("Welcome to the Python Cookbook !")
	show_options()
	selection()


if __name__ == '__main__':
	main()