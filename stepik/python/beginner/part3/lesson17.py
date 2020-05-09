from numpy import *

a = array([2, 3, 4])
print(a)
print()
print(a.ndim) # array size
print()
print(a.shape) # amount of rows and columns
print()
b = array([(1.5, 2, 3), (4, 5, 6)])
print(b)
print()
print(b.ndim) # array size
print()
print(b.shape) # amount of rows and columns
print()
print(b.size)
print()
z = zeros((3, 2))
print(z)
print()
c = arange(10, 30, 5)
print(c)
print()
d = linspace(0, 2, 9)
print(d)
print()
e = arange(12).reshape(4, 3)
print(e)
print()
f = array([10, 20, 30])
g = arange(3)
print(f + g) # sum arrays
print(f - g) # minus arrays
print(f ** 2)
h = 2 * sin(f)
print(h)
print(f < 20)