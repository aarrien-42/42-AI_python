def check(f):
	def final(self, x):
		if type(x) != list or not x:
			return None
		return f(self, x)
	return final

class TinyStatistician:
	@check
	def mean(self, x):
		return float(sum(x) / len(x))
	@check
	def median(self, x):
		return float(sorted(x)[len(x) // 2])
	@check
	def quartiles(self, x):
		x.sort()
		return [self.median(x[0:len(x)//2]), self.median(x[len(x)//2:])]
	@check
	def var(self, x):
		return sum([(i - self.mean(x))**2 for i in x])/len(x)
	@check
	def std(self, x):
		return self.var(x)**0.5




x = TinyStatistician()
a = [1, 42, 300, 10, 59]
print(x.mean(a))
print(x.median(a))
print(x.quartiles(a))
print(x.var(a))
print(x.std(a))