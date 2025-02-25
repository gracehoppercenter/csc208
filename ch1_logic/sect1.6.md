# Section 1.6: Chapter Summary Exercises


## Exercise 1

Complete a truth table for the statement $\lnot P \rightarrow (Q \land R)$.
> ```
> +-------+-------+-------+-------------------+
> |   p   |   q   |   r   |  ~p => (q and r)  |
> |-------+-------+-------+-------------------|
> | True  | True  | True  |       True        |
> | True  | True  | False |       True        |
> | True  | False | True  |       True        |
> | True  | False | False |       True        |
> | False | True  | True  |       True        |
> | False | True  | False |       False       |
> | False | False | True  |       False       |
> | False | False | False |       False       |
> +-------+-------+-------+-------------------+
> ```


## Exercise 2

Suppose you know that the statement "if Peter is not tall, then Quincy is fat,
and Robert is skinny" is false. What, if anything, can you conclude about Peter
and Robert if you know that Quincy is indeed fat? Explain.

> The for an implication to be false, the conclusion must be false and the
> hypothesis must be true.  The conclusion is a conjunction, and we know that
> one of the conjuncts is true, so the other must be false (i.e. Robert is not
> skinny). We also know that the hypothesis must be true, so Peter is not
> tall.


## Exercise 3

Are the statements $P \rightarrow (Q \lor R)$ and
$(P \rightarrow Q) \lor (P \rightarrow R)$ logically equivalent?

> Looking at the following truth table:
> ```
> +-------+-------+-------+-----------------+------------------------+
> |   p   |   q   |   r   |  p => (q or r)  |  (p => q) or (p => r)  |
> |-------+-------+-------+-----------------+------------------------|
> | True  | True  | True  |      True       |          True          |
> | True  | True  | False |      True       |          True          |
> | True  | False | True  |      True       |          True          |
> | True  | False | False |      False      |         False          |
> | False | True  | True  |      True       |          True          |
> | False | True  | False |      True       |          True          |
> | False | False | True  |      True       |          True          |
> | False | False | False |      True       |          True          |
> +-------+-------+-------+-----------------+------------------------+
> ```
> we can see that they are logically equivalent. Alternatively, we can reason
> that a disjunction (like the second of these two statements) is false if and
> only if both disjuncts are false. Each of the disjuncts are implications,
> which are false only if they hypothesis is true and the conclusion is false.
> That means only when $Q$ is false, $R$ is false, and $P$ is true will both
> of these statements be false.


## Exercise 4

Is the following a valid deduction rule? Explain.
```math
\begin{array}{c}
P \rightarrow Q \\
P \rightarrow R \\
\hline
\therefore P \rightarrow (Q \land R).
\end{array}
```
> We discussed this already in our
> [Propositional Logic test](PropositionalLogicTestSolutions.md), where it
> was given as problem 2. 


## Exercise 5

Write the negation, converse and contrapositive for each of the statements
below.

### Part (a)

If the power goes off, then the food will spoil.

> Let P: The power goes off, and S: The food spoils. This gives us
> $P \rightarrow S$ as a sybolic representation of the statement.
> ```math
> \text{Negation: } \lnot (P \rightarrow S) \iff \lnot (\lnot P \lor S) \iff
> P \land \lnot S. \\
> \text{Converse: } S \rightarrow P \\
> \text{Contrapositive: } \lnot P \rightarrow \lnot S \\
> ```
> Since it was negation that gave us the most challenge on the last test,
> it would do us well to train our intuition by focusing on it here.
> Translating the symbolic negation back into English gives us:
> "The power goes off and the food does not spoil."  Think about it until
> you can convince yourself that this is indeed the negation of the assertion
> that if the power goes off the food will spoil.

### Part (b)

If the door is closed, then the light is off.

> Let D: The door is closed, and L: The light is off. This gives us
> $D \rightarrow L$ as a sybolic representation of the statement.
> ```math
> \text{Negation: } \lnot (D \rightarrow L) \iff \lnot (\lnot D \lor L) \iff
> D \land \lnot L. \\
> \text{Converse: } L \rightarrow D \\
> \text{Contrapositive: } \lnot L \rightarrow \lnot D \\
> ```

### Part (c)

$\forall x (x < 1 \rightarrow x^2 < 1)$.

> Let P(x): $x < 1$, and Q(x): $x^2 < 1$. Our statement translate into
> $\forall x (P(x) \rightarrow Q(x))$. Let S: $P(x) \rightarrow Q(x)$.
> The negation of $\forall x S(x)$ is $\exists x \lnot S(x)$ (i.e. A proof
> by counterexample can be used when asserting something holds for everything). 
> $\lnot S(x)$ is $\lnot (P(x) \rightarrow Q(x)) \iff \lnot P(x) \land Q(x)$. 
> This translates back to: $\exists x (x < 1 \land x^2 \ge 1)$.
> All we need is one such x, which is not difficult to find
> ($x = -2$ will work).
