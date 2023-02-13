from vector import Vector

x = Vector([[1.], [2.], [3.], [4.]])
y = Vector([[3.], [2.], [3.], [5.]])
z = Vector([[3., 5., 3.]])
n = Vector([[1., 0., 6.]])
print("--------------------")
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
print("--------------------")
s1 = Vector(3)
s2 = Vector(3)
s3 = Vector(3)
print(f"s1 = {s1}")
print(f"s2 = {s2}")
print(f"s3 = {s3}")
r1 = Vector(3, 7)
r2 = Vector(0, 10)
r3 = Vector(-2, 1)
print(f"r1 = {r1}")
print(f"r2 = {r2}")
print(f"r3 = {r3}")