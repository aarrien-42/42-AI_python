from vector import Vector

x = Vector([[1.], [2.], [3.], [4.]])
y = Vector([[3.], [2.], [3.], [5.]])

z = Vector([[3., 5., 3.]])
n = Vector([[1., 0., 6.]])

print(f"x = {x}")
print(f"y = {y}")
print(f"z = {z}")
print(f"n = {n}")

print(f"x trans = {x.T()}")
print(f"z trans = {z.T()}")

print("--------------------")

print(f" x = {x.values}\n y = {y.values}")
print(f" z = {z.values}\n n = {n.values}")
print(f"x.y = {x.dot(y)}")
print(f"z.n = {z.dot(n)}")
print(f"x+y = {x+y}")
print(f"z+n = {z+n}")
print(f"x-y = {x-y}")
print(f"z-n = {z-n}")
print(f"x*5 = {x*5}")
print(f"z*3 = {z*3}")
print(f"x/5 = {x/5}")
print(f"z/2 = {z/3}")