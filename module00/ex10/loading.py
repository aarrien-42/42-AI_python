from time import sleep
from tqdm import tqdm

def ft_progress(listy):
	return 0

listy = range(1000)
ret = 0
for elem in ft_progress(listy):
	ret += (elem + 3) % 5
	sleep(0.01)
print()
print(ret)