import sys

if len(sys.argv) != 3 or type(sys.argv[1]) != str or sys.argv[2].isnumeric() == False:
	exit(print("ERROR"))
S = sys.argv[1]
N = int(sys.argv[2])
S = S.split()
S = [i.replace(",", "") for i in S]
words = []
for word in S:
	if len(word) > N:
		words.append(word)
print(words)
