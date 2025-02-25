# Section 2.2: Arithmetic and Geometric Sequences 


## Exercise 1: Consider the sequence $5, 9, 13, 17, 21,...$ with $a_1 = 5$

### Part (a): Give a recursive definition for the sequence. 

> The value of each element is four more than the element that proceeded it,
> so a recursive definition for it is: $a_n = a_{n - 1} + 4$ with $a_0 = 5$. 

### Part (b): Give a closed formula for the $nth$ term of the sequence. 

> Arithmetic sequences are described by linear equations defined on the set
> of natural numbers (using $\N_0$ will make things simpler for us). From our
> high school algebra course, we can recognize the difference between
> successive elements as the *slope* of the equation, and the value of the
> first element of the sequence (this is where starting from $0$ make things
> easier) as the *intercept*. The closed formula for our sequence here is
> thus: $a_n = 4n + 5$.

### Part (c): Is $2013$ a term in the sequence? Explain. 

> If $2013$ is a term in our sequence then $2013 = 4n + 5$ for some value
> $n \in \N_0$.  Solving for $n$ gives us $n = 502$, so $2013$ is a term
> in our sequence. 

### Part (d): How many terms does the sequence $5, 9, 13, 17, 21,...,533$ have? 

> Using the same process as in part c above, we get $a_{132} = 533$, and since
> we are starting from the $0^{th}$ term, there are $133$ terms in this
> sequence. 

### Part (e): Find the sum $5 + 9 + 13 + 17 + ... + 533$. Show your work.

> From part d above, we determined that there are 133 addends in this sum.
> The terms whose subscripts add to $132$ ($a_0$ and $a_132$, $a_1$ and
> $a_131$, $a_2$ and $a_130$, etc.) all sum to $538$ ($5 + 533$, $9 + 528$,
> $13 + 523$, etc.). So by add this sequence to itself with these pairings,
> and then dividing the result by $2$ to remove the duplication, we get a
> total sum of $\frac{133 \cdot 538}{2} = 35777$.

### Part (f): Use what you found above to find $b_n$, the $n^{th}$ term of $1, 6, 15, 28, 45,...$, where $b_0 = 1$

> The sequence of differences between terms in this sequence is
> $5, 9, 13, 17, ...$.  The differences between terms in this sequence is
> constant ($4$), so we are looking at an arithmetic sequence for the
> differences between terms, and a *sequence of partial sums* for the 
> originial sequence. Let's write out this sequence of partial sums.
$$
\begin{align*}
b_0 &= 1 \\
b_1 &= 1 + 5 \\
b_2 &= 1 + 5 + 9 \\
b_3 &= 1 + 5 + 9 + 13 \\
b_4 &= 1 + 5 + 9 + 13 + 17 \\
\vdots \\
b_n &= 1 + 5 + 9 + ... + (4n + 1) 
\end{align*}
$$
The partial sums beginning with the second term is our sequence $a_n$. To
create a closed formula for this, let's use a technique we have already seen.
$$
\begin{array}{cccccccccc}
  & 5 & + & 9 & + & ... & + & {4n - 3} & + & {4n + 1} \\
+ & {4n + 1} & + & {4n - 3} & + & ... & + & 9 & + & 5 \\
\hline
  & {4n + 6} & + & {4n + 6} & + & ... & + & {4n + 6} & + & {4n + 6} \\
\end{array}
$$
Giving us a closed formula for $b_n$ of: 
$$
b_n = 1 + \frac{n(4n + 6)}{2}
$$


## Exercise 2: Consider the sequence $(a_n)_{n \ge 0}$, which starts with $8, 14, 20, 26,...$

### Part (a): What is the next term in the sequence? 

> Each term is 6 more than the last, so the next term is $32$.

### Part (b): Find a formula for the $n\text{th}$ term of this sequence.

> $a_n = 6n + 8$

### Part (c): Find the sum of the first 100 terms of the sequence: $\sum_{k=0} ^{99} a_k$.

> The last term is: $a_{99} = 6(99 + 1) + 2 = 602$, so the sum of the first
> 100 terms is: $\frac{100 \cdot 610}{2} = 30500$.


## Exercise 3: Consider the sum $4 + 11 + 18 + 25 + ... + 249$

### Part (a): How many terms (summands) are in the sum? 

> The $n\text{th}$ summand is given by the forumla $s_n = 7n - 3$.
> If $7n - 3 = 249$, $n = 36$, and there are 37 (we started at 0) terms in the
> sum.

### Part (b): Compute the sum using a technique discussed in this section. 

>



## Exercise 4: Consider the sequence $1, 7, 13, 19, ..., 6n + 7$ 

### Part (a): How many terms are there in the sequence? 

>

### Part (b): What is the second-to-last term? 

>

### Part (c): Find the sum of all the terms in the sequence, in terms of $n$. 

>

