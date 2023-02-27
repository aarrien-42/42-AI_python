import time
from random import randint
import os

def write_log(action, time):
	f = open("machine.log", "a")
	f.write(f"({os.environ['USER']})Running: {' '.join([i.capitalize() for i in action.split('_')]).ljust(20)}")
	if time < 1.0:
		f.write(f"[ exec-time = {(time*1000):.3f} ms ]\n")
	else:
		f.write(f"[ exec-time = {time:.3f} s ]\n")
	f.close()

def log(f):
	def decorador_real(self, *args):
		st = time.time()
		if f.__name__ == "add_water":
			value = f(self, args[0])
		else:
			value = f(self)
		et = time.time()
		write_log(f.__name__, et - st)
		return value
	return decorador_real


class CoffeeMachine():
	water_level = 100

	@log
	def start_machine(self):
		if self.water_level > 20:
			return True
		else:
			print("Please add water!")
		return False

	@log
	def boil_water(self):
		return "boiling..."

	@log
	def make_coffee(self):
		if self.start_machine():
			for _ in range(20):
				time.sleep(0.1)
				self.water_level -= 1
			print(self.boil_water())
			print("Coffee is ready!")

	@log
	def add_water(self, water_level):
		time.sleep(randint(1, 5))
		self.water_level += water_level
		print("Blub blub blub...")

if __name__ == "__main__":
	machine = CoffeeMachine()
	for i in range(0, 5):
		machine.make_coffee()
	machine.make_coffee()
	machine.add_water(70)
