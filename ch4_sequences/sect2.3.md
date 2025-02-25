# Section 2.3: Polynomial Fitting 


## Exercise 1 

Use polynomial fitting to find the formula for the $n\text{th}$ term of the
sequence $(a_n)_{n \ge 0}$ which starts,
```math
s = 0, 2, 6, 12, 20,...
```
> The sequence of differences for this sequence is $2, 4, 6, 8,...$, which
> is a *linear sequence*, and thus the sequence of second differences is
> constant. By our rule for finite differences, the closed formula for this
> sequence is thus quadratic, $s_n = an^2 + bn + c$. From $s_0 = 0$ we get
> $c = 0$. This gives $s_1 = 2 = a + b$ and $s_2 = 6 = 4a + 2b$. Combining
> these two equations we get $2b = 6 - 4(2 - b)$ or $b = 1$, and $a = 1$.
> Our closed formula is thus: $s_n = n^2 + n$.


## Exercise 2 

Use polynomial fitting to find the formula for the $n\text{th}$ term of the
sequence $(a_n)_{n \ge 0}$ which starts,
```math
s = 1, 2, 4, 8, 15, 26,...
```
> The sequence of differences is $1, 2, 4, 7, 11,...$. The sequence of
> second differences is $1, 2, 3, 4,...$, and the sequence of third
> differences is a constant, so $s$ is $\Delta^3$-constant, and we are looking
> at a polynomial of degree 3. We need to find $a$, $b$, $c$, and $d$ for
> $s_n = an^3 + bn^2 + cn + d$. From $s_0$ we get $d = 1$, so we can use the
> following system of equations to find $a$, $b$, and $c$:
```math
\begin{array}{rrrrrrrl}
a & + & b & + & c & = & 1 & (e1) \\
8a & + & 4b & + & 2c & = & 3 & (e2) \\
27a & + & 9b & + & 3c & = & 7 & (e3) \\
 & & 4b & + & 6c & = & 5 & (e4 = -8 \cdot e1 + e2)(-1) \\
 & & 18b & + & 24c & = & 20 & (e5 = -27 \cdot e1 + e3)(-1) \\
 & & b & & & = & 0 & (e6 = -4 \cdot e4 + e5)(\frac{1}{2}) \\
 & & & & c & = & \frac{5}{6} & (e7 = \frac{1}{6} \cdot e4 \enspace
 \text{with e6 substitution}) \\
a & & & & & = & \frac{1}{6} & (e8 \enspace
\text{e1 with e6 and e7 substitutions})
\end{array}
```
> As many programmers would tell you "arithmetic is for computers, not for
> people", we could get Python to do all the above work for us:
```python
from sympy import *

init_printing()
A = Matrix([[1, 1, 1], [8, 4, 2], [27, 9, 3]])
B = Matrix([1, 3, 7])
pprint(A)
print('times')
pprint(B)
print('equals')
X = A.inv() * B
pprint(X)
```
> This will pretty print the following:
```
⎡1   1  1⎤
⎢        ⎥
⎢8   4  2⎥
⎢        ⎥
⎣27  9  3⎦
times
⎡1⎤
⎢ ⎥
⎢3⎥
⎢ ⎥
⎣7⎦
equals
⎡1/6⎤
⎢   ⎥
⎢ 0 ⎥
⎢   ⎥
⎣5/6⎦
```
> In either case we arrive at the closed formula:
> $S_n = \frac{1}{6}n^3 + \frac{5}{6}n + 1$.


## Exercise 3 

Use polynomial fitting to find the formula for the $n\text{th}$ term of the
sequence $(a_n)_{n \ge 0}$ which starts,
```math
s = 2, 5, 11, 21, 36,...
```
> The sequence of differences is $3, 6, 10, 15,...$. The sequence of
> second differences is $3, 4, 5,...$, and the sequence of third
> differences is a constant, so $s$ is cubic polynomial with $d = 2$. Let's
> set up the > system of equations to find $a$, $b$, and $c$:
```math
\begin{array}{rrrrrrrl}
a & + & b & + & c & = & 3 & (e1) \\
8a & + & 4b & + & 2c & = & 8 & (e2) \\
27a & + & 9b & + & 3c & = & 18 & (e3) \\
\end{array}
```
> and let Python do the computuation for us:
```
⎡1   1  1⎤
⎢        ⎥
⎢8   4  2⎥
⎢        ⎥
⎣27  9  3⎦
times
⎡3 ⎤
⎢  ⎥
⎢9 ⎥
⎢  ⎥
⎣19⎦
equals
⎡1/6 ⎤
⎢    ⎥
⎢ 1  ⎥
⎢    ⎥
⎣11/6⎦
```
> giving us the closed formula:
> $S_n = \frac{1}{6}n^3 + n^2 + \frac{11}{6}n + 2$.


## Exercise 4 

Use polynomial fitting to find the formula for the $n\text{th}$ term of the
sequence $(a_n)_{n \ge 0}$ which starts,
```math
s = 3, 6, 12, 22, 37, 58,...
```
> Let's "cheat" a bit here and not do the computations. The system of equations
> to solve for $a$, $b$, and $c$ will be the same as they were in the previous
> exercise. The only difference will be $d = 3$. This gives us the closed
> formula: $s_n = \frac{1}{6}n^3 + n^2 + \frac{11}{6}n + 3$.


## Exercise 5 

Make up sequences that have

### part (a):  3, 3, 3, 3, ... as its second differences.

> Since the second differences are constant, the first differences will be 
> linear. We can choose $1$ as the first element in the sequence and get
> $1, 4, 7, 10, 13,...$ as the first differences. Choose $0$ as the starting
> point for the original sequence, and we get $0, 1, 5, 12, 22, 33,...$.

### part (b):  1, 2, 3, 4, 5,... as its third differences.
