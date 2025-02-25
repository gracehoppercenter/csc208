# Chapter 2.5: Induction

## Proof by Mathematical Induction

Let $p(n), \forall n \ge n_0$ where $n, n_0 \in \Z_+$ be a statement. To prove
$p(n)$ it is sufficient to:

1. show that $p(n_0)$ holds. (This is called the *base case*.)
2. show that whenever $p(k)$ with $k \ge n_0$ holds, $p(k+1)$ holds. ($p(k)$ is
   called the *inductive hypothesis*, and is assumed true in the proof by
   inducation.)

When we have established these two assertions, we can say that *by the
principle of mathematical induction*, $p(n)$ is true for all natural numbers
greater than or equal to $n_0$.
