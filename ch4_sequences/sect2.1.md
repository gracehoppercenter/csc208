# Section 2.1: Describing Sequences Exercises


## Exercise 1

> Find the closed formula for each of the following sequences by relating them
> to a well known sequence. Assume the first term given is $a_1$.

### Part (a): $2, 5, 10, 17, 26,...$

> Since the difference between successive terms is *not* constant, this is
> not an arithmetic sequence. It is also fairly easy to spot that the ratio
> of successive terms is not constant, since $\frac{2}{5} \ne \frac{1}{2}$,
> so it is not a geometric sequence. The next of the common sequences to try
> is powers of 2. Aha, 2 is one more than 1, 5 is one more than 4, and 10
> is one more than 9.  Likewise for 17 and 26.  So, the closed formula for
> this sequence is: $a_n = 2^n + 1$.

### Part (b): $0, 2, 5, 9, 14, 20,...$

> The differences between each element form a linear sequence,
> $2, 3, 4, 5, 6,...$, which is a sign of cloned form sequence that is
> [quadratic](https://en.wikipedia.org/wiki/Quadratic), like the triangular
> numbers presented in our textbook. Indeed, if we subtract 1 from each of
> the values in the triangular numbers sequence, we get this one, so our
> closed formula here is: $a_n = \frac{n(n + 1)}{2} - 1$.

### Part (c): $8, 12, 17, 23, 30,...$

> Here again we see a linear sequence in the difference between terms,
> $4, 5, 6, 7,...$, so we should look for modification of the trianglar
> numbers formula. The difference between terms sequence for the trianglar
> numbers is $2, 3, 4, 5,...$, while ours here starts at $4$. That suggests
> we look at $T_n = \frac{(n + 2)(n + 3)}{2}$, for $n \ge 1$, which would
> yield sequence $6, 10, 15, 21, 28,...$. Each value here is two less than
> in our desired sequence, so we just need to add two:
> $a_n = \frac{(n + 2)(n + 3)}{2} + 2$.

### Part (d): $1, 5, 23, 119, 719,...$

> A quick glance at this sequence reveals that it is growing *fast*, and that
> the difference between elements is growing at faster than linear, so the
> sequence itself is growing faster than quadratic, immediately ruling out
> square or triangular numbers. So it makes sense to compare this sequence
> to the faster growing ones (powers of 2, Fibonacci, and factorials). Doing
> this reveals that each element here is one less than the corresponding
> element in > the factorial numbers, starting with the second factorial
> element, so we get $a_n = (n + 1)! - 1$.
