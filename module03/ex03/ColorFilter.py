import numpy as np
import sys
sys.path.insert(1, '../ex01')
from ImageProcessor import ImageProcessor

class ColorFilter:
	def invert(self, array):
		"""Inverts the color of the image received as a numpy array."""
		return 255 - array
	def to_blue(self, array):
		"""Applies a blue filter to the image received as a numpy array."""
		new_arr = np.copy(arr)
		new_arr[:,:,(0, 1)] = 0
		return new_arr
	def to_green(self, array):
		"""Applies a green filter to the image received as a numpy array."""
		new_arr = np.copy(arr)
		new_arr[:,:,(0, 2)] = 0
		return new_arr
	def to_red(self, array):
		"""Applies a red filter to the image received as a numpy array."""
		new_arr = np.copy(arr)
		new_arr[:,:,(1, 2)] = 0
		return new_arr

if __name__ == "__main__":
	imp = ImageProcessor()
	cf = ColorFilter()
	arr = imp.load("imagen.jpeg")
	#imp.display(arr)
	i1 = cf.invert(arr)
	i2 = cf.to_blue(arr)
	i3 = cf.to_green(arr)
	i4 = cf.to_red(arr)
	i = np.concatenate((i1, i2, i3, i4), axis=1)
	imp.display(i)
