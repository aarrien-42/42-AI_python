from functools import reduce

def ft_reduce(function_to_apply, iterable):
	if callable(function_to_apply) == False:
		raise TypeError(f"'{type(function_to_apply).__name__}' object is not callable")
	if hasattr(iterable, '__iter__') == False:
		raise TypeError("ft_reduce() arg 2 must support iteration")
	res = iterable[0]
	for i in range(1, len(iterable), 2):
		res = res + function_to_apply(iterable[i], iterable[i + 1])
	return res

x = [1, 2, 3, 4, 5]
lst = ['H', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
print(reduce(lambda u, v: u + v, lst))
print(ft_reduce(lambda u, v: u + v, lst))
print(reduce(lambda u, v: u + v, x))
print(ft_reduce(lambda u, v: u + v, x))