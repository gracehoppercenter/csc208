# Section 2.5: Induction


## Exercise 1

On the way to the market, you exchange your cow for some magic dark
chocolate espresso beans. These beans have the property that every night at
midnight, each bean splits into two, effectively doubling your collection.
You decide to take advantage of this and each morning (around 5 am) you eat
5 beans.

### Part (a)

Expain why it is true that *if* at noon on day $n$ you have a number of beans
ending in a 5, that at noon on day $n + 1$ you will still have a number of
beans ending in a 5.

>

### Part (b)

Why is the previous fact not enough to conclude that you will always have a
number of beans ending in a 5? What additional fact would you need?

>

### Part (c)

Assuming you have the additional fact in part (b), and have successfully proved
the fact in part (a), how do you know that you will always have a number of
beans ending in a 5? Illustrate what is going on by carefully explaining how
the two facts above prove that you will have a number of beans ending in a 5
on *day 4* specifically. In other words, explain why induction works in this
context.


## Exercise 2

Use induction to prove for all $n \in \N$ that
$\sum_{k=0}^n 2^k = 2^{n+1} - 1$. 

> $2^0 = 1 = 2^1 - 1$, so we have our base case.  Assume the induction
> hypothesis, that $\sum_{k=0}^n 2^k = 2^{n+1} - 1$ for some $k \in \N$. We
> need to show that $\sum_{k=0}^{n+1} 2^k = 2^{(n+1)+1} - 1$. By definition
> of a sum, $\sum_{k=0}^{n+1} 2^k = \sum_{k=0}^{n} 2^k + 2^{n+1}$. By our
> induction hypothesis, we know this equals $2^{n+1} - 1 + 2^{n+1}$.
> Rearranging and combining terms, we get
> $2^1 \cdot 2^{n+1} - 1 = 2^{(n + 1) + 1} - 1$.  Thus by the principle of
> mathematical induction, $\sum_{k=0}^n 2^k = 2^{n+1} - 1$ for all $n \in N$. 


## Exercise 3

Prove that $7^n - 1$ is a multiple of $6$ for all $n \in \N$.

>


## Exercise 4

Prove that $1 + 3 + 5 + ... + (2n - 1) = n^2$ for all $n \ge 1$.

>


## Exercise 5

Prove that $F_0 + F_2 + F_4 + ... + F_{2n} = F_{2n+1} - 1$ where $F_n$ is the
$n\text{th}$ Fibonacci number.

>


## Exercise 6

Prove that $2^n < n!$ for all $n \ge 4$.

>


## Exercise 7

Prove, by mathematical inducation, that
$F_0 + F_1 + F_2 + ... + F_n = F_{n+2} - 1$, where $F_n$ is the $n\text{th}$
Fibonacci number.

>


# Exercise 8

Zombie Euler and Zombie Cauchy, two famous zombie mathematicians, have just
signed up for Twitter accounts. After one day, Zombie Cauchy has more followers
than Zombie Euler. Each day after that, the number of new followers of Zombie
Cauchy is exactly the same as the number of new followers of Zombie Euler (and
neither lose any followers). Explain how a proof by mathematical induction can
show that on every day after the first day, Zombie Cauchy will have more
followers than Zombie Euler. That is, explain what the base case and inductive
case are, and why they together prove that Zombie Cauchy will have more
followers on the 4th day.

>


# Exercise 9

Find the largest number of points which a football team cannot get exactly
using just 3-point field goals and 7-point touchdowns (ignore the possibilities
of safeties, missed extra points, and two point conversions). Prove your answer
is correct by mathematical induction.

>


# Exercise 10

Prove that the sum of $n$ squares can be found as follows
$$
1^2 + 2^2 + 3^2 + ... + n^2 = \frac{n(n + 1)(2n + 1)}{6}
$$

>


# Exercise 11

Prove that the sum of the interior angles of a convex $n\text{-gon}$ is
$(n - 2) \cdot 180^{\circ}$.
