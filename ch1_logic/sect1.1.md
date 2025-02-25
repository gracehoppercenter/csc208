# Section 1.1: Propositional Logic Exercises


## Exercise 1

Consider the statement about a party, "If it's your birthday or there will be
cake then there will be cake."

### Part (a)

Translate the above statement into symbols. Clearly state which statement is
$P$ and $Q$.

> $P$: It is your birthday. $Q$: There will be cake.
> **Statement**: $P \lor Q \rightarrow Q$.
> 
> Since *implications are disjunctions*, our statement here is logically
> equivalent to $\lnot (P \lor Q) \lor Q$, which by De Morgan's Law is
> equivalent to $(\lnot P \land \lnot Q) \lor Q$. 

### Part (b)

Make a truth table for the statement.

> Here is a useful truth table for this statement:
> ```
> +-------+-------+-------------+----------------+--------------------+
> |   p   |   q   |  ~p and ~q  |  p or q  => q  |  (~p and ~q) or q  |
> |-------+-------+-------------+----------------+--------------------|
> | True  | True  |    False    |      True      |        True        |
> | True  | False |    False    |     False      |       False        |
> | False | True  |    False    |      True      |        True        |
> | False | False |    True     |      True      |        True        |
> +-------+-------+-------------+----------------+--------------------+
> ```
> Since the last two columns have the same truth values, the orignial
> statement and the final one are logically equivalent.

### Part (c)

Assuming the statement is true, what (if anything) can you conclude if there
will be cake?

> If $Q$ is true, we learn nothing about $P$. 

### Part (d)

Assuming the statement is true, what (if anything) can you conclude if there
will not be cake?

> If $Q$ is false, then the statement is only true if $P$ is also false,
> so it's not your birthday.

### Part (e)

Suppose you found out that the statement was a lie. What can you conclude?

> With $\lnot (\lnot P \land \lnot Q) \lor Q)$, using De Morgan's laws
> we get $(P \lor Q) \land \lnot Q$, which is only true when $P$ is true and
> $Q$ is false. So it is your birthday, but you'll have to go without cake :-(


## Exercise 2

Make a truth table for the statement $(P \lor Q) \rightarrow (P \land Q)$.

> ```
> +-------+-------+----------+-----------+-------------------------+
> |   p   |   q   |  p or q  |  p and q  |  (p or q) => (p and q)  |
> |-------+-------+----------+-----------+-------------------------|
> | True  | True  |   True   |   True    |          True           |
> | True  | False |   True   |   False   |          False          |
> | False | True  |   True   |   False   |          False          |
> | False | False |  False   |   False   |          True           |
> +-------+-------+----------+-----------+-------------------------+
> ```
>
> This table demonstrates that the given statement is logically equivalent to
> an [exclusive or](https://en.wikipedia.org/wiki/Exclusive_or), represented
> by the $\oplus$ operator.


## Exercise 3

Make a truth table for the statement $\lnot P \land (Q \rightarrow P)$. What
can you conclude about $P$ and $Q$ if you know the statement is true?

> ```
> +-------+-------+-------+----------+-------------------+
> |   p   |   q   |  ~p   |  q => p  |  ~p and (q => p)  |
> |-------+-------+-------+----------+-------------------|
> | True  | True  | False |   True   |       False       |
> | True  | False | False |   True   |       False       |
> | False | True  | True  |  False   |       False       |
> | False | False | True  |   True   |       True        |
> +-------+-------+-------+----------+-------------------+
> ```
>
> This statement is only true when both $P$ and $Q$ are false. This makes
> intuitive sense, since implications are disjunctions, so ${Q \rightarrow P}$
> is logically equivalent to $\lnot Q \lor P$, which if $P$ is false, can only
> be true if $Q$ is false.


## Exercise 4

Make a truth table for the statement $\lnot P \rightarrow (Q \land R)$.

> ```
> +-------+-------+-------+-------+-----------+-------------------+
> |   p   |   q   |   r   |  ~p   |  q and r  |  ~p => (q and r)  |
> |-------+-------+-------+-------+-----------+-------------------|
> | True  | True  | True  | False |   True    |       True        |
> | True  | True  | False | False |   False   |       True        |
> | True  | False | True  | False |   False   |       True        |
> | True  | False | False | False |   False   |       True        |
> | False | True  | True  | True  |   True    |       True        |
> | False | True  | False | True  |   False   |       False       |
> | False | False | True  | True  |   False   |       False       |
> | False | False | False | True  |   False   |       False       |
> +-------+-------+-------+-------+-----------+-------------------+
> ```


## Exercise 5

Geoff Poshingten is out at a fancy pizza joint, and decides to order a calzone.
When the waiter asks what he would like in it, he replies, "I want either
pepperoni or sausage. Also, if I have sausage, then I must also include quail.
Oh, and if I have pepperoni or quail then I must also have ricotta cheese."

### Part (a)

Translate Geoff's order into logical symbols.

> Let $P$: Calzone has pepperoni, $S$: Calzone has sauage,
> $Q$: Calzone has quail, and $R$: Calzone has ricotta cheese. Translating
> "or" statements from English is ambigouus, but the use of "either-or" here
> suggests an exclusive or.  With that interpretation, our statements
> are: $(P \lor S) \land \lnot (P \land S)$, $S \rightarrow Q$,
> $(P \lor Q) \rightarrow R$.

### Parts (b and c)

The waiter knows that Geoff is either a liar or a truth-teller (so either
everything he says is false, or everything is true). Which is it? What,
if anything, can the waiter conclude about the ingredients in Geoff's
desired calzone?

> ```
> +-------+-------+-------+-------+----------------------------------------------+
> |   p   |   s   |   q   |   r   |  (p xor s) and (s => q) and ((p or q) => r)  |
> |-------+-------+-------+-------+----------------------------------------------|
> | True  | True  | True  | True  |                    False                     |
> | True  | True  | True  | False |                    False                     |
> | True  | True  | False | True  |                    False                     |
> | True  | True  | False | False |                    False                     |
> | True  | False | True  | True  |                     True                     |
> | True  | False | True  | False |                    False                     |
> | True  | False | False | True  |                     True                     |
> | True  | False | False | False |                    False                     |
> | False | True  | True  | True  |                     True                     |
> | False | True  | True  | False |                    False                     |
> | False | True  | False | True  |                    False                     |
> | False | True  | False | False |                    False                     |
> | False | False | True  | True  |                    False                     |
> | False | False | True  | False |                    False                     |
> | False | False | False | True  |                    False                     |
> | False | False | False | False |                    False                     |
> +-------+-------+-------+-------+----------------------------------------------+
> ```
> There are three situations where Geoff gets what he wants. A calzone with
> pepperoni and ricotta, with or without quail, but no sausage; and one with
> sausage, quail, and ricotta, but not pepperoni. 


## Exercise 6

Determine whether the following two statements are logically equivalent:
$\lnot ({P \rightarrow Q})$ and $(P \land \lnot Q)$. Explain how you know
you are correct.

> With *implications are disjunctions*, we established by truth table that
> $P \rightarrow Q$ is logically equivalent to $\lnot P \lor Q$. By
> *De Morgan's Law* this is in turn logically equivalent to $P \land \lnot Q$.
>
> The truth table confirms this:
> ```
> +-------+-------+-------------+--------------+
> |   p   |   q   |  ~(p => q)  |  (p and ~q)  |
> |-------+-------+-------------+--------------|
> | True  | True  |    False    |    False     |
> | True  | False |    True     |     True     |
> | False | True  |    False    |    False     |
> | False | False |    False    |    False     |
> +-------+-------+-------------+--------------+
> ```


##  Exercise 7

Are the statements $P \rightarrow (Q \lor R)$ and
$(P \rightarrow Q) \lor (P \rightarrow Q)$ logically equivalent?
