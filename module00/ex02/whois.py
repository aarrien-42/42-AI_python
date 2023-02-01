import sys

if len(sys.argv) == 1:
	print("")
elif len(sys.argv) > 2:
	print("AssertionError: more than one argument are provided")
elif sys.argv[1].isdigit() == False:
	print("AssertionError: argument is not an integer")
else:
	if sys.argv[1] == '0':
		print("I'm Zero")
	elif int(sys.argv[1])%2 == 0:
		print("I'm Even")
	else:
		print("I'm Odd")