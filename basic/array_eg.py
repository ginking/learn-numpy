from numpy import *

# generate a list and reshape to multi array
a = arange(15).reshape(3, 5)
print(a)
b = arange(8).reshape(2, 2, 2)
print(b)
print("=========================")

# show the shape of array
print(a.shape)
print(b.shape)
print("=========================")

# dimension of array
print(a.ndim)
print(b.ndim)
print("=========================")

# type of elements in array
print(a.dtype)
print(b.dtype)
print("=========================")

# init array with data type
c = array([['1','2'], ['3', '4']], dtype=str)
print c

#
d = linspace(0, 2 * math.pi, 8)
print(d)