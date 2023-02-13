from book import Book
from recipe import Recipe
import time

a = Recipe("Tortilla", 3, 30, ["Patata", "Huevo", "Sal"], "", "lunch")
b = Recipe("Huevos rotos", 8, 10, ["Huevos"], "", "lunch")
x = Book("RECETAS", {"starter":[], "lunch":[], "dessert":[]})
x.add_recipe(a)
x.add_recipe(0)
x.get_recipe_by_types("lunch")
time.sleep(1)
x.add_recipe(b)
print(x)
