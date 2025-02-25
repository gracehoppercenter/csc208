# Chapter 1.4: Proofs

## Proof of Euclid's Theorem

[Euclid's theorem](https://en.wikipedia.org/wiki/Euclid%27s_theorem) is the
fundemental statement in
[number theory](https://en.wikipedia.org/wiki/Number_theory) that there are
infinitely many prime numbers, a proof of which is presented at the beginning
of this section in our text.

Here is a presentation that is a variation of the proof Euclid gave himself:

We first need to establish the following theorem: *If a is an integer that
divides two other integers b and c, then a also divides b - c*. We can prove
this as follows:

* Since $a$ divides $b$, there exists another integer $m$ such that
  $b = a \cdot m$.
* Likewise, since $a$ divides $c$, there exists an integer $n$ such that
  $c = a \cdot n$.
* $b - c = am - an = a(m - n)$.
* Since $m$ and $n$ are both integers and since integers are closed under
  subtraction, $m - n$ is an integer and $a$ divides $b - c$.

Now on to our proof of Euculid's algorithm.

* Assume there are only finitely many primes, $p_1, p_2, ..., p_n$.
* Let $P = p_1 \cdot p_2 \cdot ... \cdot p_n$ be the product of all of these
  primes.
* Let $Q = P + 1$.
* By our assumption, $Q$ must not be prime, since it is greater than $P$,
  and therefore greater than all the primes in our exhaustive list of primes
  that form the product $P$.
* But $Q$ must be prime, since if it were not prime it would have one of
  the primes in our list, let's call it $p_k$ as a factor, and $p_k$ would
  thus divide both $P$ and $Q$, and therefore it would divide $Q - P = 1$.
  There is no prime number that divides $1$, so assuming $Q$ is not prime
  leads to a contradiction, and we can conclude that there are infinitely
  many primes.


## Proof Techniques 

### Direct Proof

To directly prove the implication $P \rightarrow Q$, you can *assume* $P$,
and then *arrive at* $Q$ through a sequence of valid logical steps.

### Mini Sudoku Definitions

A **mini sudoku puzzle** is a partially filled in 4 x 4 grid of squares,
divided into four 2 x 2 boxes. Each square can be empty or contain a digit from
1 to 4.

We say that a mini sudoku puzzle is **valid** provided no digit from 1 to 4
appears more than once in any row, any column, or any box.

A **solution** to a mini sudoku puzzle with no empty squares and every
non-empty square of the puzzle unchanged.

We say that a mini sudoku puzzle is **solvable** if there is exactly one
solution.

### Mini Sudoku Solution Proposition

Any solution to a mini sudoku puzzle will have each digit from 1 to 4 appear
exactly once in each row, column, and box, appearing a total of four times in
the puzzle.


### Proof by Contrapositive

An implication $P \rightarrow Q$ is *logically equivalent* to its
contrapositive, $\lnot Q \rightarrow \lnot P$, so proving the contrapositive
is logically equivalent to proving the original statement.

The example in our text, proving that *if $n$ is even, $n^2$ is even*, provides
an excellent example of where this technique can be helpful.


### Proof by Contradiction

The idea behind this approach stated in formal logic terms is to prove
$P$ by proving $\lnot P \rightarrow Q$ where $Q$ can be shown to be false,
giving us $\lnot (\lnot P)$ (by contrapositve), which is the negation of a
negation, and thus true.

The first example in the text is the wonderful proof that the $\sqrt{2}$ is
irrational.

Prove that $\sqrt{2}$ is irrational.

**Proof**. Suppose that $\sqrt{2}$ is not irrational (this is our $\lnot P$ ).
Then $\sqrt{2}$ is rational, which means it can be written as the ratio of two
integers $a$ and $b$, where $b \ne 0$, which we can assume
[WOLOG](https://en.wikipedia.org/wiki/Without_loss_of_generality) to be reduced
to lowest terms (this is our $Q$ ). Thus,

$$
2 = \frac{a^2}{b^2} \\
2b^2 = a^2.
$$

So $a^2$ is even, and we can conclude $a$ is even, and it can be written
as $a = 2k$ for some integer $k$. Squaring both sides yields $a^2 = 4k^2$. We
then have,

$$
2b^2 = 4k^2 \\
b^2 = 2k^2.
$$

This means $b^2$ is even, and thus $b$ is even. Now we have $a$ and $b$ both
even, contradicting our valid assumption that $\frac{a}{b}$ was in lowest
terms (this is our $\lnot (\lnot P)$. Thus, assuming that $\sqrt{2}$ is
rational leads to a contradiction, and it can not therefore be true, and we
can conclude that $\sqrt{2}$ is irrational.
[Q.E.D.](https://en.wikipedia.org/wiki/Q.E.D.). 


### Proof by (Counter) Example 

This technique must be used carefully, in specific cases:

* To prove $\exists x P(x)$ it is sufficient to *find one* such $x$.
* To disprove $\forall x P(x)$ it is sufficient to *find one* $x$ where 
  $\lnot P(x)$ holds. 


### Proof by Cases 

The idea here is that when you are trying to prove that something holds over
*all* elements within a domain (all rational numbers, for example), it can
sometimes be easier to
[partition](https://en.wikipedia.org/wiki/Partition_of_a_set) the domain and
then prove the assertion on each subset of the partition.

#### Example

I can recall often utilizing
[trichotomy](https://en.wikipedia.org/wiki/Law_of_trichotomy), especially with
proofs in [calculus](https://en.wikipedia.org/wiki/Calculus), using this
approach as an undergraduate majoring in mathematics.

I'll provide an example establishing a result for
[rational numbers](https://en.wikipedia.org/wiki/Rational_number), which can
be represented by a computer, rather than
[irrational numbers](https://en.wikipedia.org/wiki/Irrational_number), which
can not.

**Theorem**: Given any two rational numbers $a$ and $b$ with $a \ne b$, there
exists a rational number $r$ that is between them.

**Proof**: By trichotomy and the assumption that $a \ne b$, we know that
either $a > b$ or $a < b$. Let us assume WOLOG that $a < b$, and that thus
$b - a > 0$.  By the
[Archimedean property](https://en.wikipedia.org/wiki/Archimedean_property),
there exists a positive integer $n$ such that $\frac{1}{n} < b - a$. 

Let $r = a + \frac{1}{n}$. Since $n$ is positive, $\frac{1}{n}$ is positive,
and thus $\frac{1}{n} > 0$ and $a + \frac{1}{n} > a$.

Since $\frac{1}{n} < b - a$, $a + \frac{1}{n} < b$. Since $a$ is a rational
number and rational numbers are closed under addition, $r$ is a rational
number and we have found a number $r$ such that $a < r < b$, making $r$ between
$a$ and $b$. Q.E.D.


### Summary of Proof Styles 

To prove an implication $P \rightarrow Q$:

| Style              | Start                             | End                     |
|--------------------|-----------------------------------|------------------------|
| **Direct**         | Assume $P$.                       | Therefore $Q$.          |
| **Contrapositive** | Assume $\lnot Q$                  | Therefor $\lnot P$.     |
| **Contradiction**  | Assume $\lnot (P \rightarrow Q)$. | *reductio ad absurdum*. |
