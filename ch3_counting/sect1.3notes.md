# Section 1.3: Combinations and Permutations 

## Permutation

A **permutation** is a (possible) rearrangement of objects. For example, the
six permutations of the letters a, b, and c are:

> abc, acb, bac, bca, cab, cba

### Permutations of $n$ elements

There are
```math
n! = n \cdot (n - 1) \cdot (n - 2) \cdot ... \cdot 2 \cdot 1
```
permutations of $n$ (distinct) elements.


### $k \text{-permutations}$ of $n$ elements

$P(n, k)$ is the number of **$k \text{-permutations}$ of $n$ elements**, the
number of ways to arrange $k$ objects chosen from $n$ distinct objects.

```math
P(n, k) = \frac{n!}{(n - k)!} = n(n - 1)(n - 2)...(n - (k - 1))
```

### Closed formula for ${n}\choose{k}$

```math
{n\choose k} = \frac{n!}{(n - k)!k!} \
= \frac{n(n - 1)(n - 2)...(n - (k - 1))}{k(k - 1)(k - 2)...1}
```
