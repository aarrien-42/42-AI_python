import sys

numbers = sys.argv[1:]
if len(numbers) == 0:
	exit(print("Usage: python operations.py <number1> <number2>"))
elif len(numbers) > 2:
	exit(print("AssertionError: too many arguments"))
elif len(numbers) < 2:
	exit(print("AssertionError: too few arguments"))
for i in numbers:
	if i.isnumeric() == False:
		exit(print("AssertionError: only integers"))
num1 = int(numbers[0])
num2 = int(numbers[1])
print(f"Sum:		{num1+num2}")
print(f"Difference:	{num1-num2}")
print(f"Product:	{num1*num2}")
if num2 != 0:
	print(f"Quotient:	{num1/num2}")
	print(f"Remainder:	{num1%num2}")
else:
	print("Quotient:	{}".format("ERROR (division by zero)"))
	print("Remainder:	{}".format("ERROR (modulo by zero)"))
