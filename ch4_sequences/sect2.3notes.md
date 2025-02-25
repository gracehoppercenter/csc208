# Chapter 2.3: Polynomial Fitting 


## Sequences of Differences

A **sequence of differences** is the sequence of the differences between
subsequent elements of a sequence.  Given the sequence:
```math
s = a_0, a_1, a_2, a_3, a_4,...
```
the sequence of differences is the sequence:
```math
s_{diff} = a_1 - a_0, a_2 - a_1, a_3 - a_2, a_4 - a_3,...
```
The sequence of **second differences** is the sequence formed by taking the
the differences between subsequent elements of $s_{diff}$, and the sequence
of **third differences** is the sequence formed by taking the differences
between subsequent elements of the sequence of second differences, and
so forth.


## Finite Differences

The close formula for a sequence will be a degree $k$ polynomial if and only
if the $k\text{th}$ sequence of differences is constant.  We call such a
sequence $\Delta^k$-constant. 


## Resources

* [Solving Systems of Linear Equations with Python's Numpy](https://stackabuse.com/solving-systems-of-linear-equations-with-pythons-numpy/)
