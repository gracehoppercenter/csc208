# Discrete Math Propositional Logic Test

1. Determine if the statements $P \rightarrow (Q \lor R)$ and
   $(P \rightarrow Q) \lor (P \rightarrow R)$ are logically equivalent.

> From the following truth table:
>
> ```
> +-------+-------+-------+-----------------+-----------------------+
> |   p   |   q   |   r   |  p => (q or r)  |  (p = q) or (p => r)  |
> |-------+-------+-------+-----------------+-----------------------|
> | True  | True  | True  |      True       |         True          |
> | True  | True  | False |      True       |         True          |
> | True  | False | True  |      True       |         True          |
> | True  | False | False |      False      |         False         |
> | False | True  | True  |      True       |         True          |
> | False | True  | False |      True       |         True          |
> | False | False | True  |      True       |         True          |
> | False | False | False |      True       |         True          |
> +-------+-------+-------+-----------------+-----------------------+
> ```
>
> we see that the two statements have the same truth values, and are therefore
> logically equivalent.


2. Prove the following:
   ```math
   \begin{array}{c}
   P \rightarrow Q \\
   \noindent\uline{P \rightarrow R} \hfill \\
   \therefore P \rightarrow (Q \land R).
   \end{array}
   ```

> From the following truth table:
> ```
>  +-------+-------+-------+----------+----------+------------------+
>  |   p   |   q   |   r   |  p => q  |  p => r  |  p => (q and r)  |
>  |-------+-------+-------+----------+----------+------------------|
>  | True  | True  | True  |   True   |   True   |       True       |
>  | True  | True  | False |   True   |  False   |      False       |
>  | True  | False | True  |  False   |   True   |      False       |
>  | True  | False | False |  False   |  False   |      False       |
>  | False | True  | True  |   True   |   True   |       True       |
>  | False | True  | False |   True   |   True   |       True       |
>  | False | False | True  |   True   |   True   |       True       |
>  | False | False | False |   True   |   True   |       True       |
>  +-------+-------+-------+----------+----------+------------------+
> ```
> we can see that the final statement is true whenever the two hypotheses
> are true, so the conclusion follows from the hypotheses.
>
> Alternatively, we can establish this using
> [rules of inference](https://en.wikipedia.org/wiki/List_of_rules_of_inference).
>
> ```math 
> \begin{array}{lll}
> (1) & P \rightarrow Q & \text{Given} \\ 
> (2) & P \rightarrow R & \text{Given} \\ 
> (3) & P & \text{conditional proof assumption} \\
> (4) & Q & \text{(1), (3), modus ponens} \\
> (5) & R & \text{(2), (3), modus ponens} \\
> \noindent\uline{(6) & Q \land R & \text{(4), (5), adjunction}} \hfill \\
> \therefore & P \rightarrow (Q \land R) & \text{(3) and (6)}
> \end{array}
> ``` 


3. Using the statement: *If you read for understanding and work all the
   exercises you will score well on the test.*  Translate it into symbols,
   then write its **negation**, **converse**, and **contrapositive**.
   What can you conclude if you don't score well on the test?

> Let $R$: You read for understanding; $W$: You work all exercises; and
> $S$: You score well on the test. The given statement translates into symbols
> as:
> ```math
> (R \land W) \rightarrow S
> ```
> The negation, converse, and contrapostive statements are as follows:
> ```math
> \text{Negation: } R \land W \land \lnot S \\
> \text{Converse: } S \rightarrow (R \land W) \\
> \text{Contrapositive: } \lnot S \rightarrow (\lnot R \lor \lnot W) \\
> ```
> Using the contrapositive, which is logically equivalent to the original
> statement, you can conclude that if you don't score well on the test, then
> you didn't read for understanding *or* you didn't work all the exercises.
>
> Many of the submissions had ambigous wording, like "you didn't read for
> understanding and work all the exercises." I understand that the intention
> here is $\lnot (R \land W)$, rather than $\lnot R \land W$, but it is
> clearer to say "you didn't read for understanding *or* you didn't work all
> the exercises. Learning logic can help us write clearer arguments.
>
> The **contrapositive** is logically equivalent to the original expression,
> as we can see here:
>
> ```
> +-------+-------+-------+------------------+------------------+
> |   r   |   w   |   s   |  (r and w) => s  |  ~s => ~r or ~w  |
> |-------+-------+-------+------------------+------------------|
> | True  | True  | True  |       True       |       True       |
> | True  | True  | False |      False       |      False       |
> | True  | False | True  |       True       |       True       |
> | True  | False | False |       True       |       True       |
> | False | True  | True  |       True       |       True       |
> | False | True  | False |       True       |       True       |
> | False | False | True  |       True       |       True       |
> | False | False | False |       True       |       True       |
> +-------+-------+-------+------------------+------------------+
> ```
> It is clear from the class results that the **negation** was the most
> misunderstood. In looking at the various incorrect responses, I realize we
> have a "teachable moment" here.
>
> The best (and easiest) way to think about the negation of an expression is
> to simply enclose the given expression in parentheses and prepend it with
> the negation operator. We can see that this works from the following truth
> table.
>
> ```
> +-------+-------+-------+------------------+---------------------+
> |   r   |   w   |   s   |  (r and w) => s  |  ~((r and w) => s)  |
> |-------+-------+-------+------------------+---------------------|
> | True  | True  | True  |       True       |        False        |
> | True  | True  | False |      False       |        True         |
> | True  | False | True  |       True       |        False        |
> | True  | False | False |       True       |        False        |
> | False | True  | True  |       True       |        False        |
> | False | True  | False |       True       |        False        |
> | False | False | True  |       True       |        False        |
> | False | False | False |       True       |        False        |
> +-------+-------+-------+------------------+---------------------+
> ```
> Since *implications are disjunctions*, the negation expression can
> simplified to $R \land W \land \lnot S$ (try it). When grading test
> submissions, I made a truth table of the various proposed negations
> submitted, and found most of them did not work as intended.
>
> A few of you learned the following little ditty from one of your math
> teachers:
> ```
> * converse -> switch
> * inverse -> negate
> * contrapositive -> switch & negate
> ```
> *Thanks, Marin!* ;-)
>
> The missing piece in your understanding mostly stemmed from incorrectly
> concluding that the negation of $(R \land W) \rightarrow S$ is
> $\lnot (R \land W) \rightarrow \lnot S$. It isn't:
> ```
> +-------+-------+-------+---------------------+--------------------+
> |   r   |   w   |   s   |  ~((r and w) => s)  |  ~(r and w) => ~s  |
> |-------+-------+-------+---------------------+--------------------|
> | True  | True  | True  |        False        |        True        |
> | True  | True  | False |        True         |        True        |
> | True  | False | True  |        False        |       False        |
> | True  | False | False |        False        |        True        |
> | False | True  | True  |        False        |       False        |
> | False | True  | False |        False        |        True        |
> | False | False | True  |        False        |       False        |
> | False | False | False |        False        |        True        |
> +-------+-------+-------+---------------------+--------------------+
> ```
> Study this truth table, and reflect on the insights you can learn from it
> regarding *boolean expressions*, *implications*, and *negations*.

