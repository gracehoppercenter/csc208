# Chapter 2.1: Describing Sequences 


## Closed forumula 

A **closed formula** for a sequence $({a_n})_{n \in \mathbb{N}}$ is a formula
for $a_n$ using a fixed finite number of operations on $n$.


## Recursive definition 

A **recursive definition** (sometimes called an **inductive definition**) for
a sequence $({a_n})_{n \in \mathbb{N}}$ consists of a **recurance relation**:
an equation relating a term of the sequence to previous terms (terms with a
smaller index) and an **initial condition**: a list of a few terms of the
sequence (one less than the number of terms in the recurrance relation). 


## Common Sequences 

### Square numbers

The **square numbers** are
the sequence of numbers $({s_n})_{n \ge 1}$ defined by the closed
formula $s_n = n^2$.
```math
1, 4, 9, 16, 25, ...
```

### Triangular numbers

The **triangular numbers** are the sequence of numbers
$({T_n})_{n \ge 1}$ defined by the closed formula
$T_n = \frac{n(n - 1)}{2}$.
```math
1, 3, 6, 10, 15, 21, ...
```

### Powers of 2 

The **powers of 2** is the sequence $(a_n)_{n \ge 0}$ with closed formula
$a_n = 2^n$.
```math
1, 2, 4, 8, 16, 32,...
```

### Fibonacci Numbers 

The **fibonacci numbers** (or
[Fibonacci sequence](https://en.wikipedia.org/wiki/Fibonacci_sequence)) are
the sequence of numbers defined recursively by $F_n = F_{n-1} + F_{n-2}$ with
$F_1 = F_2 = 1$.
```math
1, 1, 2, 3, 5, 13, 21, 34, 55, 89, 144,... 
```

### Factorial Numbers 

A [factorial](https://en.wikipedia.org/wiki/Factorial) is a non-negative
integer, denoted by $n!$, whose value is the product of all non-negative
integers less than or equal to it.
```math
n! = n \times (n - 1) \times (n - 2) \times ... \times 3 \times 2 \times 1
```
Recursively, this can be written $n! = n \cdot (n - 1)!$ with $a_n = 1$.

The **factorial numbers** are the sequence of numbers defined by this
function. 
```math
1, 2, 6, 24, 120, 720, 5040, 40320, 362880,...
```


## Sequence of Partial Sums

Given any sequence $({a_n})_{a \in \mathbb{N}}$, we can always form a new
sequence  $({b_n})_{b \in \mathbb{N}}$ by
```math
b_n = a_0 + a_1 + a_2 + ... + a_n
```
Since the terms of $(b_n)$ are the sums of the terms of the initial part of
the sequence $(a_n)$, we call $(b_n)$ the **sequence of partial sums** of
$(a_n)$.
To simplify the writing of partial sums, we use the notation
```math
\sum_{k=1} ^{n} a_k
```
which represents the sum of the terms $a_k$ with $k$ going from $1$ to $n$.

Since the orginial sequence is defined on the infinite set of natural numbers,
the sequence of partial sums is likewise infinite. We call this infinite
sequence of partial sums a
[series](https://en.wikipedia.org/wiki/Series_(mathematics)).

We have an analogous notation for the infinite sequence of products of the
elements of a sequence.
```math
\prod_{k=1} ^{n} a_k
```
which is an alternative way of writing $n!$.


## Resources

* [Sigma and Pi Notation (Summation and Product Notation)](https://mathmaine.com/2010/04/01/sigma-and-pi-notation/)
