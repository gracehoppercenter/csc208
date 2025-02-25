# Chapter 2.4: Solving Recurrence Relations 


## Solving a Recurrence Relation

Finding a function of $n$ (i.e. a *closed formula*) that satisfies a recurrence
relation is called **solving the recurrence relation**.

> **NOTE**: You have probably been using the phrase *satisfy an equation*
> throughout your study of math without ever seeing a formal definition of it.
> What precisely does it mean "to satisfy" an equation?  I like to think of it
> this way: equations are not *satisfied* unless they are true. So to "satisfy" 
> an equation involving variables $x$ and $y$, such as $y = 3x + 5$ means to
> find values for $x$ and $y$ ($x = 1$ and &y = 8$, for example) that "solve"
> (a synonmy of satisfy) the equation. The set of all combinations of values
> that satisfy the equation is called the **solution set**.


## Telescoping Series

A [telescoping series](https://en.wikipedia.org/wiki/Telescoping_series) is
a [series](https://en.wikipedia.org/wiki/Series_(mathematics)) whose general
term, $t_n$, is the difference of two consecutive terms of a
[sequence](https://en.wikipedia.org/wiki/Sequence), $a_n$, so that
$t_n = a_{n+1} - a_n$.


## Characteristic Roots

Given a recurrence relation $a_n + \alpha a_{n-1} + \beta a_{n-2} = 0$, the
**charactistic polynomial** is
```math
x^2 + \alpha x + \beta
```
giving the **characteristic equation**:
```math
x^2 + \alpha x + \beta = 0
```
If $r_1$ and $r_2 are two distinct roots of the characteristic polynomial, then
the solution to the recurrance relation is
```math
a_n = a r^n_1 + b r^n_2
```
where $a$ and $b$ are constants determined by these initial conditions.


## Characteristic Root Technique for Repeated Roots

Suppose the recurrence relation $a_n = \alpha a_{n-1} + \beta a_{n-2}$ has a
characteristic polynomial with only one root $r$. Then the solution to the
recurrence relation is
```math
a_n = ar^n + bnr^n
```
where $a$ and $b$ are constants determined by the initial conditions.
