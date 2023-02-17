
def ft_filter(function_to_apply, iterable):
	if callable(function_to_apply) == False:
		raise TypeError(f"'{type(function_to_apply).__name__}' object is not callable")
	if hasattr(iterable, '__iter__') == False:
		raise TypeError("ft_filter() arg 2 must support iteration")
	return (i for i in iterable if function_to_apply(i))

x = [1, 2, 3, 4, 5]
print(list(filter(lambda dum: not (dum % 2), x)))
print(list(ft_filter(lambda dum: not (dum % 2), x)))
print(list(filter(lambda dum: dum + 1, x)))
print(list(ft_filter(lambda dum: dum + 1, x)))