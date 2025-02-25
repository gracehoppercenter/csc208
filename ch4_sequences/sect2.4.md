# Section 2.4: Solving Recurrence Relations 


## Exercise 1

Find the next two terms in $(a_n)_{n \ge 0}$ beginning
$3, 5, 11, 21, 43, 85,...$ Then give a recursive definition for the sequence.
Finally, use the characteristic root technique to find a closed formula for the
sequence.

> $11 = 2 \cdot 3 + 5$. $21 = 2 \cdot 5 + 11$. $43 = 2 \cdot 11 + 21$, and
> $85 = 2 \cdot 21 + 43$.  That means the recursive definition for this
> sequence is $a_n = 2a_{n-2} + a_{n-1}$, and the next two terms in the
> sequence are $171$ and $341$. Rewriting this recurrence relation as
> $a_n - a_{n-1} - 2a_{n-2} = 0$, we have get the *characteristic polynomial*
> $x^2 + -x + -2$ and the *characteristic equation* $x^2 + -x + -2 = 0$.
> or $(x + 1)(x - 2) = 0$, giving us $r_1 = -1$ and $r_2 = 2$. So the solution
> to the recurrence relation will be of the form
> $a_n = a \cdot(-1)^n + b \cdot 2^n$ for some constants $a$ and $b$.
> Using the first two values of the sequence as the intial conditions, we
> can solve for $a$ and $b$. $3 = a + b$ and
> $5 = -a + 2b$. $b = \frac{8}{3}$ and $a = \frac{1}{3}$, and the closed
> formula for this sequence is:
```math
a_n = \frac{8 \cdot (-1)^n + 2^n}{3}
```

## Exercise 2
