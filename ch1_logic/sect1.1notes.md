# Section 1.1: Mathematical Statements 


## Logical Connectives 

We define the following **logical connectives**.

* $P \land Q$ is read "P and Q," and is called a **conjunction**.
* $P \lor Q$ is read "P or Q," and is called a **disjunction**.
* $P \rightarrow Q$ is read "if P then Q," and is called an **impliation** or
  **conditional**.
* $P \leftrightarrow Q$ is read "P if and only if Q," and is called a
  **biconditional**.
* $\lnot P$ is read "not P," and is called a **negation**.


## Truth Conditions for Connectives 

The **truth condidtions** for the logical connectives are defined at follows.

* $P \land Q$ is true when both $P$ and $Q$ are true.
* $P \lor Q$ is true when $P$ or $Q$ or both are true.
* $P \rightarrow Q$ is true when $P$ is false or $Q$ is true (or both). 
* $P \leftrightarrow Q$ is true $P$ and $Q$ both true, or both false.
* $\lnot P$ is true when $P$ is false. 


## Truth Tables 

Each of the preceding definitions can be represented in a [truth
table](https://en.wikipedia.org/wiki/Truth_table).

> **Note**
> The following tables where generated using
> [truth-table-generator](https://pypi.org/project/truth-table-generator/)

```
       CONJUNCTION
+-------+-------+-----------+
|   P   |   Q   |  P and Q  |
|-------+-------+-----------|
| True  | True  |   True    |
| True  | False |   False   |
| False | True  |   False   |
| False | False |   False   |
+-------+-------+-----------+

       DISJUNCTION 
+-------+-------+----------+
|   P   |   Q   |  P or Q  |
|-------+-------+----------|
| True  | True  |   True   |
| True  | False |   True   |
| False | True  |   True   |
| False | False |  False   |
+-------+-------+----------+

      IMPLICATION
+-------+-------+----------+
|   P   |   Q   |  P => Q  |
|-------+-------+----------|
| True  | True  |   True   |
| True  | False |  False   |
| False | True  |   True   |
| False | False |   True   |
+-------+-------+----------+

      BICONDITIONAL
+-------+-------+---------+
|   P   |   Q   |  P = Q  |
|-------+-------+---------|
| True  | True  |  True   |
| True  | False |  False  |
| False | True  |  False  |
| False | False |  True   |
+-------+-------+---------+
```


## Logical Equivalence

Two (molecular) statements $P$ and $Q$ are **logically equivalent**
provided $P$ is true precisely when $Q$ is true. That is, $P$ and $Q$ have the
same truth value under any assignment of truth values to their atomic parts
(i.e. They have the same truth table).


## De Morgan's Laws
```math
\lnot(P \land Q) \text{ is logically equivalent to }
\lnot P \lor \lnot Q \text{.}\\
\lnot(P \lor Q) \text{ is logically equivalent to }
\lnot P \land \lnot Q \text{.}
```


## Implications are Disjunctions
```math
P \rightarrow Q \text{ is logically equivalent to } \lnot P \lor Q \text{.}
```


## Negation of an Implication
```math
\lnot (P \rightarrow Q) \text{ is logically equivalent to }
P \lor \lnot Q \text{.}
```


## Predicate Logic

[Predicate Logic](https://en.wikipedia.org/wiki/First-order_logic) is a
formal language that uses
[quantified variables](https://en.wikipedia.org/wiki/Quantifier_(logic))
and [predicates](https://www.merriam-webster.com/dictionary/predicate) to
construct statements.

For example:
```
P(x): x is prime.
O(x): x is odd.
```
```math
\forall x((P(x) \land x > 2) \rightarrow O(x)) \text{.}
```

## Quantifiers

The **universal quantifier** is written $\forall$ and is read "for all." The
**existential quantifier** is written $\exists$ and is read, "there exists" or
"for some."


## Every This is a That

Any statement of the form, "Every $P$-thing is a $Q$-thing" can be written as
$$
\forall x(P(x) \rightarrow Q(x)).
$$
For example, "All mammals have hair," becomes
$$
\forall x(M(x) \rightarrow H(x))
$$
where $M(x)$ means $x$ is a mammal, and $H(x)$ means $x$ has hair.


## A Least One This is a That

Statements of the form, "There exists a $P$-thing that is a $Q$-thing,"
"A least one $P$-thing is a $Q$-thing," or "Some $P$-things are $Q$-things,"
can be written
$$
\exists x(P(x) \land Q(x)).
$$
For example, "Some cats can swim," becomes
$$
\exists x(C(x) \land S(x))
$$
where $C(x)$ means $x$ is a cat, and $S(x)$ means $x$ can swim.


## Universal Generalization 

Given a sentence with free variables, the **universal generalization** of that
sentence is the statement obtained by adding enough universal quantifiers to
the beginning of the sentence so that all free variables become bound.
