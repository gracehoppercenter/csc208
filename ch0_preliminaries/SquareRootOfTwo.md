# The Square Root of 2 Is Irrational

We want to prove that $\sqrt{2}$ is an irrational number. Our strategy will
be to use *proof by contradiction*, assuming that $\sqrt{2}$ is rational and
then showing how this leads to a contradiction.


## First, a helpful theorem

Before getting to that, we will need to establish the following theorem.

>  If $a^2$ is even, then $a$ is even.

*Proof:*

Using our notation for sets an **even number** is
$\{x \in \mathbb{N} : \exists n \in \mathbb{N} (x = 2n)\}$, and an
**odd number** is
$\{x \in \mathbb{N} : \exists n \in \mathbb{N} (x = 2n + 1)\}$.

We want to prove that if $a^2$ is even, then $a$ is even.  The best approach
is to prove the *contrapositive*, which as we know is logically equivalent.

We need to prove that if $a$ is not even (meaning it's odd), then
$a^2$ is odd.  We assume $a$ is odd. That means that
$\exists k \in \N : 2 k + 1 = a$. Squaring this gives us $(2k + 1)^2$, which
equals $4k^2 + 4k + 1$. We can factor 2 out of the first two term, giving us
$2(2k^2 + 2k) + 1$.  Since the set of integers is closed under both
[multiplication](https://proofwiki.org/wiki/Integer_Multiplication_is_Closed)
and
[addition](https://proofwiki.org/wiki/Integer_Addition_is_Closed),
$2k^2 + 2k$ is an integer, which we can all $m$. We can then rewrite our $a^2$
as $2m + 1$, which by definition is an odd number.


## On to our proof... 

Assume $\sqrt{2}$ is *not* irrational, which means that it is rational and
can be written as $p\over q$, where $p$ and $q$ are
[coprime](https://en.wikipedia.org/wiki/Coprime_integers) integers
and $q \neq 0$.  

Squaring both sides of the equation $\sqrt{2}$ = $p\over q$ gives us
$2$ = $p^2 \over q^2$.  Multiplying both sides by $q^2$, we have
$2q^2$ = $p^2$. By the
[fundamental theorem of arithmetic](https://en.wikipedia.org/wiki/Fundamental_theorem_of_arithmetic),
since $2q^2$ and $p^2$ are equal, they have the same prime factors. Since 2 is
one of these factors, $p^2$ is even, and by the theorem we proved at the
start of this discussion, $p$ must therefore also be even. That means $p$ can
be written as $2k$ for some $k \in \mathbb{N}$.

Substituting $2k$ for $p$ in $2q^2$ = $p^2$ we get $2q^2$ = $(2k)^2$ which
gives us $2q^2$ = $4k^2$. Dividing both sides by 2, we get
$q^2$ = $2k^2$.  That means $q^2$ is even, and by our same theorem, $q$ is
even.

This means that both $p$ and $q$ are even, meaning they have a common factor,
2, contradicting that they are coprime.

Since assuming that the $\sqrt{2}$ is rational leads to a contradiction
(see
[reductio ad absurdum](https://en.wikipedia.org/wiki/Reductio_ad_absurdum)),
we have proven that the $\sqrt{2}$ is irrational.


## Resources

* [ChiliMath: Prove: The Square Root of 2 is Irrational](https://www.chilimath.com/lessons/basic-math-proofs/prove-square-root-of-2-is-irrational/)
* [ChiliMath Prove: If n squared is even, then n is even](https://www.chilimath.com/lessons/basic-math-proofs/if-n-squared-is-even-then-n-is-even/)
