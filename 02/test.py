from vector import Vector


print(Vector([[0.0], [1.0], [2.0], [3.0]]).shape)
print(Vector([0.0, 1.0, 2.0, 3.0]).shape)

v1 = Vector([[0.0], [1.0], [2.0], [3.0]])
v2 = Vector([[1.0], [1.5], [2.7], [3.8]])
print((v1 + v2).values)

print("v1: ", v1)
print("v1.t(): ", v1.T())
print("v1 + v2: ", v1 + v2)
print("v1 - v2: ", v1 - v2)
print("v1 * v2: ", v1 * 2.0)
print("v1 / v2: ", v1 / 2.0)

print("v1.dot(v2): ", v1.dot(v2))