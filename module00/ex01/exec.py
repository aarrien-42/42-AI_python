import sys

print((' '.join(i[::-1] for i in sys.argv[:0:-1])).swapcase())
print(' '.join(sys.argv[1:])[::-1].swapcase())