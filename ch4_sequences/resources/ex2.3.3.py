from sympy import *


init_printing()
A = Matrix([[1, 1, 1], [8, 4, 2], [27, 9, 3]])
B = Matrix([3, 9, 19])
X = A.inv() * B
pprint(A)
print('times')
pprint(B)
print('equals')
pprint(X)
