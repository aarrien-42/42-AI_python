
def	ft_map(function_to_apply, iterable):
	if callable(function_to_apply) == False:
		raise TypeError(f"'{type(function_to_apply).__name__}' object is not callable")
	if hasattr(iterable, '__iter__') == False:
		raise TypeError("ft_map() arg 2 must support iteration")
	return (function_to_apply(i) for i in iterable)

x = [1, 2, 3, 4, 5]
print(map(lambda dum: dum + 1, x))
print(list(map(lambda dum: dum + 1, x)))
print(ft_map(lambda dum: dum + 1, x))
print(list(ft_map(lambda dum: dum + 1, x)))

