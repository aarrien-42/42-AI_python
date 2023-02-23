class CsvReader():
	def __init__(self, filename=None, sep=',', header=False, skip_top=0, skip_bottom=0):
		try:
			f = open(filename, "r")
		except OSError:
			print("Error: cannot open", filename)
			return None
		self.r = [i.split(sep) for i in f.read().split('\n')]
		f.close()
		self.h = None
		if header == True:
			self.h = self.r.pop(0)
		for i in range(skip_top):
			self.r.pop(0)
		l = len(self.r)
		for i in range(skip_bottom):
			self.r.pop(l - i - 1)
	def __enter__(self):
		try:
			x = self.r
		except:
			return None
		return self
	def __exit__(self, exc_type, exc_val, exc_tb):
		return self
	def getdata(self):
		return self.r
	def getheader(self):
		return self.h

with CsvReader("homes.cs") as file:
	if file == None:
		print("File is corrupted")

with CsvReader("homes.csv") as file:
	print(f"data = {file.getdata()}")
	print(f"header = {file.getheader()}") 