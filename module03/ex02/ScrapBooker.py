import numpy as np

class ScrapBooker:
	def crop(self, array, dim, position=(0,0)):
		"""Crops the image as a rectangle via dim arguments
		(being the new height and width of the image) from the coordinates given by position arguments."""
		if position[0] + dim[0] >= len(array) or position[1] + dim[1] >= len(array[0]):
			return None
		new_arr = np.array([row[position[1]:position[1] + dim[1]] for row in array[position[0]:position[0] + dim[0]]])
		return new_arr
	def thin(self, array, n, axis):
		"""Deletes every n-th line pixels along the specified axis (0: vertical, 1: horizontal)"""
		if axis == 0:
			r = range(n - 1, len(array[0]), n)
			new_arr = np.delete(array, r, 1)
		if axis == 1:
			r = range(n - 1, len(array), n)
			new_arr = np.delete(array, r, 0)
		return new_arr
	def juxtapose(self, array, n, axis):
		"""Juxtaposes n copies of the image along the specified axis."""
		if axis == 0:
			new_arr = np.tile(array, (n, 1))
		if axis == 1:
			new_arr = np.tile(array, (1, n))
		return new_arr
	def mosaic(self, array, dim):
		"""Makes a grid with multiple copies of the array. The dim argument specifies
		the number of repetition along each dimensions."""
		return np.tile(array, dim)

if __name__ == "__main__":
	x = ScrapBooker()
	arr1 = np.arange(0,25).reshape(5,5)
	print(f"ORIGINAL:\n{arr1}")
	print(f"CROP\n{x.crop(arr1, (3, 1), (1, 0))}")
	arr2 = np.array("A B C D E F G H I".split() * 6).reshape(-1,9)
	print(f"ORIGINAL:\n{arr2}")
	print(f"THIN\n{x.thin(arr2, 3, 0)}")
	arr3 = np.array([[1, 2, 3], [1, 2, 3], [1, 2, 3]])
	print(f"ORIGINAL:\n{arr3}")
	print(f"JUXTAPOSE\n{x.juxtapose(arr3, 3, 1)}")
	print(f"ORIGINAL:\n{arr1}")
	print(f"MOSAIC\n{x.mosaic(arr1, (3, 2))}")