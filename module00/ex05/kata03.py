kata = "The right format"
#print(kata.rjust(42, "-"), end='')
print(f"{kata:->42}", end='')