# Chapter 1.5: Proofs about Discrete Structures

## Subsets, Supersets, and Proper Subsets

A set $A$ is a **subset** of a set $B$, written $A \subseteq B$, provided
every element of $A$ is also an element of $B$.

The set $B$ is sometimes called a **superset** of $A$.

We say $A$ is a **proper subset** of $B$, written $A \subset B$ and $A \neq B$.
In other words, if every element in $A$ is an element $B$, and there is at
least on element in $B$ that is *not* in $A$.


## Subset is a Transitive Relation

For any sets $A$, $B$, and $C$, if $A \subseteq B$ and $B \subseteq C$,
then $A \subseteq C$.


## Definition: Injective (One-to-One) Functions

A function $f : A \rightarrow B$ is **injective** (or **one-to-one**) provided
every element in $B$ is the image of at most one element in $A$. In other words,
no element in $B$ is the *output* of more than one *input* from $A$.


## A Larger Set Cannot Be Injective on a Smaller Set

Suppose $f : A \rightarrow B$ is a function with $A$ and $B$ both finite sets.
If $\vert A \vert > \vert B \vert$, the $f$ is *not* injective.


## Definition: Image of a Set Under a Function

Given a function $f : X \rightarrow Y$ and a set $A \subseteq X$, we define the
**image of A under f** to be the set $f(AP = \{f(a) \in Y : a \in A\}$. That
is, $f(A)$ is the set of all outputs of the function for inputs in $A$.


## The Image of a Subset is a Subset of the Image of Its Superset

Let $f : X \rightarrow Y$ be a function, and let $A$ and $B$ be subsets of $X$.
If $A \subseteq B$, then $f(A) \subseteq f(B)$.


## Relations

A **relation** on a set $A$ is a set of ordered pairs of elements from $A$.


### Trasitive Relations

A relation $R$ on a set $A$ is **transitive** provided for all $x, y, z \in A$,
if $xRy$ and $yRz$, then $xRz$.


## Graphs

A **graph** is a set $V$ of **vertices** and a set $E$ of **edges**,
two-element subsets of the vertices.


### Degree of a Graph

Let $v$ be a vertex in a graph $G$. The **degree** of $v$, written $d(v)$, is
the number of edges that contain $v$, i.e. the number of edges *incident* to
$v$.
