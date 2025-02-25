# Section 2.6: Chapter Review 


## Exercise 1

Find the sum $3 + 7 + 11 + ... + 427$.

> Since the sequence of differences between elements of this sequence is
> constant (4), it is an *arithmetic sequence*. To find its sum, we can
> reverse and add. $(427 - 3) / 4 = 106$, so there are $106$ terms starting
> with $a_1 = 7$.  Reversing and adding we get
> $\frac{106 \cdot 434}{2} + 3= 23005$.


## Exercise 2

Consider the sequence $2, 6, 10, 14, ..., 4n + 6$.

### part (a)

How many terms are there in the sequence?

> $a_n$ = $a_{n-1} + 4$ is a recursive formula for this arithmetic sequence,
> with $a_0 = 2$, and $a_n = 4n + 2$ is a closed formula for it, with
> $n \ge 0$. Since the sequence starts with $a_0$, $a_n$ is the
> $(n + 1)\text{th}$ term in the sequence. Since the last term here,
> $4n + 6$, is the $a_{n+1}$ term (4 more than $a_n$), the number of terms
> in this sequence is $n + 2$. 

### part (b)

What is the second-to-last term?

> As discussed above, the second to last term is $4n + 2$.

### part (c)

Find the sum of all the terms in the sequence.

> $\frac{(n + 2)(4n + 8)}{2} = (n + 2)(2n + 4) = 2n^2 + 8n + 8$


## Exercise 3

Consider the sequence given by $a_n = 2 \cdot 5^{n-1}$.

### part (a)

Find the first 4 terms of the sequence. Is this sequence arithmetic, 
geometric, or neither?

> The first 4 terms are $2, 10, 50, 250$. Since the sequence of
> differences between the terms of this sequence is not constant, it is
> not linear. Since the ratio of successive terms is constant, it
> is geometric.

### part (c)

Find the sum of the first 25 terms.

$$
\begin{array}{ccccccccccccc}
  & S &= & 2 & + & 10 & + & 50 & + & ... & + & 2 \cdot 5^{24} & & \\
- & 5S &= &  &   & 10 & + & 50 & + & ... & + & 2 \cdot 5^{24} & + & 
  2 \cdot 5^{25} \\
\hline
  & -4S &= & 2 & + & 0 & + & 0 & + & ... & + & 0 & + & -2 \cdot 5^{25} \\
\end{array}
$$

> So $-4S = -2 \cdot 5^{25} + 2$, and
> $S = \frac{5^{25} + 1}{2} = 149011611938476563$. 


## Exercise 4

Consider the sequence $5, 11, 19, 29, 41, 55, ...$ starting with $a_1 = 5$.

### part (a)

Find a closed formula for $a_n$, the $n\text{th}$ term of the sequence, by
writing each term as a sum of a sequence.

> The sequence of differences for this sequence is $6, 8, 10, 12, ...$, so
> it is $\Delta^3\text{-constant}$ and the closed formula for $a_n$ will be
> a cubic polynomial.

### part (b)

Find a closed formula again, this time using either polynomial fitting or the
characteristic root technique (whichever is appropriate). Show your work.

>

### part (c)

Find a closed formula once again, this time by recognizing the sequence as a
modification to some well known sequence(s). Explain.

>
