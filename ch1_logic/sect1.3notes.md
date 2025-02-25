# Section 1.3: Rules of Logic 


## Logical Equivalence 

Two (molecular) statements $P$ and $Q$ are **logically equivalent** provided
$P$ is true precisely when $Q$ is true. That is, $P$ and $Q$ have the same
truth value under any assignment of truth values to their atomic parts
(i.e. *Their truth tables are identical*.)

We write this as $P \equiv Q$.

## Logical Equivalence of Implication and Contrapositive

An implication is logically equivalent to its contrapositive. That is,
$$
P \rightarrow Q \equiv \lnot Q \rightarrow \lnot P.
$$

## De Morgan's Laws

The negation of a disjunction or conjunction is logically equivalent to a
conjunction or disjunction of negations, respectively. That is,
$$
\lnot (P \land Q) \equiv \lnot P \lor \lnot Q
$$
and,
$$
\lnot (P \lor Q) \equiv \lnot P \land \lnot Q.
$$

## Implications are Disjunctions

$$
P \rightarrow Q \equiv \lnot P \lor Q.
$$

## Double Negation

$$
\lnot \lnot P \equiv P.
$$

## Negation of an Implication

$$
\lnot (P \rightarrow Q) \equiv P \land \lnot Q.
$$

That is, the only way for an implication to be false is for the hypothesis to
be true *and* the conclusion to be false.

