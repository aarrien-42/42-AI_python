from time import sleep
from tqdm import tqdm

def ft_progress(lst):
	for i in tqdm(lst, ascii=" >>>>>>>>>>>>>>>>>>>>>>>>>>>>>=", colour="#FF5733"):
		yield i

if __name__ == '__main__':
	listy = range(1000)
	ret = 0
	for elem in ft_progress(listy):
		ret += (elem + 3) % 5
		sleep(0.01)
	print()
	print(ret)
