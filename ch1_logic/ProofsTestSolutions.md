# CSC 208: Discrete Math Proofs Test

1. Complete the truth table for the statement:
   $\lnot (\lnot P \rightarrow (Q \land R))$.

   > ```
   > +-------+-------+-------+------------------+----------------------+
   > |   p   |   q   |   r   |  p or (q and r)  |  ~(~p => (q and r))  |
   > |-------+-------+-------+------------------+----------------------|
   > | True  | True  | True  |       True       |        False         |
   > | True  | True  | False |       True       |        False         |
   > | True  | False | True  |       True       |        False         |
   > | True  | False | False |       True       |        False         |
   > | False | True  | True  |       True       |        False         |
   > | False | True  | False |      False       |         True         |
   > | False | False | True  |      False       |         True         |
   > | False | False | False |      False       |         True         |
   > +-------+-------+-------+------------------+----------------------+
   > ```


2. Prove: if $m$ and $n$ are odd integers, then $m \cdot n$ is and odd integer.

   > Since $m$ is odd, it can be written in the form $2i + 1$ for some
   > $i \in \mathbb{Z}$. Likewise the odd value $n$ can be written as
   > $2k + 1$ for $k \in \mathbb{Z}$.
   > $m \cdot n = 4ki + 2k + 2i + 1 = 2(2ki + k + i) + 1$. Since the set of
   > integers is closed under both multiplication and addition,
   > $2ki + k + i$ is an integer (let's call it $j$), and we have
   > $m \cdot n = 2j + 1$, an odd number.
   > [Q.E.D.](https://en.wikipedia.org/wiki/Q.E.D.)

   And here is a *much* lovelier proof (more elegent and beautiful) provided by
   Caleb O'Neal:

   > Since $m$ and $n$ are both odd integers, the prime factorizations of
   > neither of them can contain a $2$, and thus the prime factorization of
   > their product, $m \cdot n$, can not contain $2$ either, and is thus odd.
   > [Q.E.D.](https://en.wikipedia.org/wiki/Q.E.D.)


3. Given 22 coins (pennies, nickels, dimes and quarters), prove the following:

   a. At least 6 of the coins must be of the same denomination.

      > Let $p$ be the number of pennies, $n$ the number of nickels,
      > $d$ the number of dimes, and $q$ the number of quarters.
      > $p + n + d + q = 22$. We want to show that $max(p, n, d, q)$ is at
      > least $6$. In other words, we are looking for the minimum value for
      > this function.  $max(p, n, d, q)$ will be minimal when the total
      > number of coins is distributed as evenly as possible among the
      > $4$ denominations.  Performing integer division dividing $22$ by
      > $4$ (``22 // 4`` in python), yields $5$. $5$ of each denomination would
      > give us a total of $20$ coins, with $2$ coins yet to be accounted for.
      > Since each of these coins must be of one of the dominations, that
      > denomination will have a $6\text{th}$ member, and at least $6$ of the
      > coins will be of the same denomination.
      > [Q.E.D.](https://en.wikipedia.org/wiki/Q.E.D.)

   b. If you have an odd number of one demonimation, you must have an odd
      number of another as well.

      > $p + n + d + q = 22$, which is an even number.  Assume, WOLOG, that
      > $p$ is odd, and assume that $n$, $d$, and $q$ are all even. Then
      > $n + d + q$ is even (let's call it $s$ ), and $p + s = 22$. But
      > $p$ is odd, and $s$ is even, and an odd and an even number sum to an
      > odd number, so they can not equal $22$, which is even. Since assuming
      > having a single odd number of one of our denominations without having
      > another leads to a contradiction, there must be an odd number of
      > another one of the denominations.
      > [Q.E.D.](https://en.wikipedia.org/wiki/Q.E.D.)
