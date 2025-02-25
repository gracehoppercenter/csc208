# Chapter 1.1: Additive and Multiplicative Principles 

## Additive Principle

If event $A$ can occur in $m$ ways, and event $B$ can occur in $n$ *disjoint*
ways, then the event $A$ or $B$ can occur in $m + n$ ways.

Stated using set notation, we have:

Given two sets $A$ and $B$, if $A \cap B = 0$, then

```math
\vert A \cup B \vert = \vert A \vert + \vert B \vert
```


## Multiplicative Principle

If event $A$ can occur in $m$ ways, and each possibility for $A$ allows exactly
$n$ ways for event $B$, then the event $A$ and $B$ can occur in
$ m \cdot n$ ways. 

Stated using set notation, given two sets $A$ and $B$ we have

```math
\vert A \times B \vert = \vert A \vert \cdot \vert B \vert
```


## Cartesian Product

Given sets $A$ and $B$, we can form the set

```math
A \times B = \{(x, y) : x \in A \land y \in B\}
```

to be the set of all ordered pairs $(x, y)$ where $x$ is an element of $A$ and
$y$ is an element of $B$. We call $A \times B$ the **Cartesian product** of
$A$ and $B$.


## Cardinality of a Union of Two Sets

For any finite sets $A$ and $B$,

```math
\vert A \cup B \vert = \vert A \vert + \vert B \vert - \vert A \cap B \vert
```


## Cardinality of a Union of Three Sets

For any finite sets $A$, $B$, and $C$,

```math
\vert A \cup B \cup C \vert = \vert A \vert + \vert B \vert + \vert C \vert
- \vert A \cap B \vert - \vert A \cap B \vert - \vert B \cap C \vert +
\vert A \cap B \cap C \vert
```
