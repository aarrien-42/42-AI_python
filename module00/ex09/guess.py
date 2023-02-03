import sys
import random

def guess():
	ran_num = random.randint(1, 99)
	num = tries = 0
	while ran_num != num:
		num = input("What's your guess between 1 and 99?\n>> ")
		tries += 1
		if num == "exit":
			exit(print("Goodbye!"))
		if num.isnumeric() == False:
			print("That's not a number")
		else:
			num = int(num)
			if num < 1 or num > 99:
				print("Out of range")
			if ran_num < num:
				print("Too high!")
			elif ran_num > num:
				print("Too low!")
	if ran_num == 42:
		print("The answer to the ultimate question of life, the universe and everything is 42.")
	if tries == 1:
		print("Congratulations, you've got it on your first try!")
	else:
		print("Congratulations, you've got it!")

print("This is an interactive guessing game!")
print("You have to enter a number between 1 and 99 to find out the secret number.")
print("Type 'exit' to end the game.")
print("Good luck!\n")

guess()