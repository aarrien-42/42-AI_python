import matplotlib.pyplot as plt
import matplotlib.image as img
import numpy as np

class ImageProcessor:
	def load(self, path):
		try:
			arr = img.imread(path)
			print(f"Loading image of dimensions {arr.shape[0]} x {arr.shape[1]}")
			return arr
		except OSError as err:
			print("OS error:", err)
		except Exception as err:
			print(f"Unexpected {err}, {type(err)}")
	def display(self, array):
		try:
			plt.imshow(array)
			plt.show()
		except:
			return 0

if __name__ == "__main__":
	x = ImageProcessor()
	img = x.load("imagen.jpeg")
	x.display(img)
	print(f"array({img})")
