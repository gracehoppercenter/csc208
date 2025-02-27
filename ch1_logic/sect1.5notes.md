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


##  Definition: Image of a Set Under a Function

Given a function $f : X \rightarrow Y$ and a set $A \subseteq X$, we define the
**image of A under f** to be the set $f(AP = \{f(a) \in Y : a \in A\}$. That
is, $f(A)$ is the set of all outputs of the function for inputs in $A$.


