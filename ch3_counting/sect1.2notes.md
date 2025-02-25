# Section 1.2: Binomial Coefficients

## Bit Strings

* An $n \text{-bitstring}$ is a bit string of length $n$.
* The **weight** of a bit string is the number of $1 \text{'s}$ it contains.
* $B^n$ is the set of all n-bit strings.
* $B^n_k$ is the set of all n-bit strings of weight $k$. 


## Recurrance Relation

A [recurrance relation](https://en.wikipedia.org/wiki/Recurrence_relation) is
an equation defining the $nth$ term of a sequence in terms of an expression
involving previous terms. Such definitions require an *initial condition*
(also called a *base case*) that defines the starting terms from which
subsequent terms can be derrived.

### Examples

1. The [Fibonacci sequence](https://en.wikipedia.org/wiki/Fibonacci_sequence)
   is defined by the equation $F_n = F_{n-1} + F_{n-2}$ with initial conditions
   $F_1 = F_0 = 1$.
2. The [Factorial](https://en.wikipedia.org/wiki/Factorial) function is
   defined by $n! = n(n-1)!$ for $n > 0$, with initial condition $0! = 1$.


## Binomial Coefficients

For each integer $n \geq 0$ and integer $k$ with $0 \leq k \leq n$, there is
a number

$${n}\choose{k}$$

read "n choose k." We have:

* ${{n}\choose{k}} = {|B^n_k|}$, the number of n-bit strings of weight k.
* ${n}\choose{k}$ is the number of subsets of size n each with cardinality k. 
* ${n}\choose{k}$ is the number of latice paths of length n containing k steps
  to the right. 
* ${n}\choose{k}$ is the coefficient of ${x}^{k}{y}^{n-k}$ in the expansion of
  ${(x + y)}^n$. 
* ${n}\choose{k}$ is the number of ways to select k objects from a total of
  n objects. 


## Recurrence Relation for Binomial Coefficient

```math
{{n}\choose{k}} = {{n-1}\choose{k-1}} + {{n-1}\choose{k}}
```


## Pascal's Triangle

Thanks to
[Math Adventures/Pascal's triangle in wiki-latex](https://en.wikiversity.org/wiki/Math_Adventures/Pascal%27s_triangle_in_wiki-latex) on
[Wikiversity](https://en.wikiversity.org/wiki/Wikiversity:Main_Page), I can
print Pascal's triangle in Markdown:

```math
\begin{array}{c}
1 \\
1 \quad 1 \\
1 \quad 2 \quad 1 \\
1 \quad 3 \quad 3 \quad 1 \\
1 \quad 4 \quad 6 \quad 4 \quad 1 \\
1 \quad 5 \quad 10 \quad 10 \quad 5 \quad 1 \\
1 \quad 6 \quad 15 \quad 20 \quad 15 \quad 6 \quad 1 \\
1 \quad 7 \quad 21 \quad 35 \quad 35 \quad 21 \quad 7 \quad 1 \\
1 \quad 8 \quad 28 \quad 56 \quad 70 \quad 56 \quad 28 \quad 8 \quad 1 \\
1 \quad 9 \quad 36 \quad 84 \quad 126
\quad 126 \quad 84 \quad 36 \quad 9 \quad 1 \\
1 \quad 10 \quad 45 \quad 120 \quad 210 \quad 252
\quad 210 \quad 120 \quad 45 \quad 10 \quad 1 \\
1 \quad 11 \quad 55 \quad 165 \quad 330 \quad 462
\quad 462 \quad 330 \quad 165 \quad 55 \quad 11 \quad 1 \\
1 \quad 12 \quad 66 \quad 220 \quad 495 \quad 792 \quad 924
\quad 792 \quad 495 \quad 220 \quad 66 \quad 12 \quad 1 \\
1 \quad 13 \quad 78 \quad 286 \quad 715 \quad 1287 \quad 1716 
\quad 1716 \quad 1287 \quad 715 \quad 286 \quad 78 \quad 13 \quad 1 \\
\end{array}
```

Here are the first six rows of Pascal's triangle generating the coefficients of
binomials raised to powers:

```math
\begin{array}{lc}
(a+b)^0= &
{\color{Red}\boldsymbol{1}} 
\\
(a+b)^1=  & 
{\color{Red}\boldsymbol{1}}a+{\color{Red}\boldsymbol{1}}b
\\
(a+b)^2=  &
{\color{Red}\boldsymbol{1}}a^2+{\color{Red}\boldsymbol{2}}ab+{\color{Red}\boldsymbol{1}}b^2
\\
(a+b)^3=  &
{\color{Red}\boldsymbol{1}}a^3+{\color{Red}\boldsymbol{3}}a^2b+{\color{Red}\boldsymbol{3}}ab^2+{\color{Red}\boldsymbol{1}}b^3
\\
(a+b)^4=  &
{\color{Red}\boldsymbol{1}}a^4+{\color{Red}\boldsymbol{4}}a^3b+{\color{Red}\boldsymbol{6}}a^2b^2+{\color{Red}\boldsymbol{4}}ab^3+ {\color{Red}\boldsymbol{1}}b^4
\\                                     
(a+b)^5=  &
{\color{Red}\boldsymbol{1}}a^5+{\color{Red}\boldsymbol{5}}a^4b+{\color{Red}\boldsymbol{10}}a^3b^2+{\color{Red}\boldsymbol{10}}a^2b^3+{\color{Red}\boldsymbol{5}}ab^4+{\color{Red}\boldsymbol{1}}b^5
\\ 
\end{array}
```

Here we see how Pascal's triangle relates to binomial coefficients:

```math
\begin{array}{c}
{\color{Red}\boldsymbol{1}}=\binom{0}{0} \\
{\color{Red}\boldsymbol{1}}=\binom{1}{0} \quad\quad{\color{Red}\boldsymbol{1}}=\binom{1}{1} \\
{\color{Red}\boldsymbol{1}}=\binom{2}{0} \quad\quad  {\color{Red}\boldsymbol{2}}=\binom{2}{1}                  
 \quad\quad{\color{Red}\boldsymbol{1}}=\binom{2}{2} \\
{\color{Red}\boldsymbol{1}}=\binom{3}{0} \quad\quad  {\color{Red}\boldsymbol{3}}=\binom{3}{1} \quad\quad 
 {\color{Red}\boldsymbol{3}}=\binom{3}{2} \quad\quad\quad\quad {\color{Red}\boldsymbol{1}}=\binom{3}{3} \\ 
{\color{Red}\boldsymbol{1}}=\binom{4}{0} \quad\quad  {\color{Red}\boldsymbol{4}}=\binom{4}{1} \quad\quad 
{\color{Red}\boldsymbol{6}}=\binom{4}{2} \quad\quad  {\color{Red}\boldsymbol{4}}=\binom{4}{3} \quad\quad 
{\color{Red}\boldsymbol{1}}=\binom{4}{4} \\
\end{array}
```
