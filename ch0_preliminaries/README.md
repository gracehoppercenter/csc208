# Chapter 0: Introduction and Preliminaries

## Jeff's Definition of Mathematics

**Mathematics**

1. The systematic study of how much / many or which one(s).

2. A game, played my mathematians.

This chapter introduces concepts and vocabulary for the study of
[logic](https://en.wikipedia.org/wiki/Logic), which may be new to you.

In order to take notes in Markdown files using plain text, we can utilize
the support on most git hosts for
[LaTeX](https://en.wikipedia.org/wiki/LaTeX) markup of mathematics.


## Is $0$ a Natural Number? 

There is no consensus among mathematicians as to whether $0$ is included
in the **natural numbers** (see [Is 0 a Natural Number: A Beginner's
Guide](https://www.storyofmathematics.com/is-0-a-natural-number/)).

Since discrete math is much about functions defined on the set of natural
numbers, this question is not trivial for us.  We will sometimes want to
include it, and sometimes not, so let's agree on the following notation:
```math
\N = \{1, 2, 3, 4, 5, ...\}
```
and *does not* contain $0$, while
```math
\N_0 = \{0, 1, 2, 3, 4, 5, ...\}
```
does.


## A Wee Bit of LaTeX

| Operator     | Command          | Output       |
|--------------|------------------|--------------|
| AND          | `$\land$`        | $\land$      |
| OR           | `$\lor$`         | $\lor$       |
| NOT          | `$\lnot$`        | $\lnot$      |
| XOR          | `$\oplus$`       | $\oplus$     |
| THEREFORE    | `$\therefore$`   | $\therefore$ |
| IMPLIES      | `$\implies$`     | $\implies$   |
| IMPLIED BY   | `$\impliedby$`   | $\impliedby$ |
| IFF          | `$\iff$`         | $\iff$       |
| IN           | `$\in$`          | $\in$        |
| SQUARE ROOT  | `$\sqrt{n}$`     | $\sqrt{n}$   |
| UNION        | `$\cup$`         | $\cup$       |
| INTERSECTION | `$\cap$`         | $\cap$       |
| VERTICAL BAR | `$\vert$`        | $\vert$      |


## Notes and Experiments

* [Truth Tables](TruthTables.md)
* [Logical Statements and Proofs](LogicalStatementsAndProofs.md)
* [The Square Root of 2 Is Irrational](SquareRootOfTwo.md)


## Resources

* [Writing mathematical expressions](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/writing-mathematical-expressions)
* [Logic operators (And, Or, Not, and Xor) in LaTeX](https://latexdoc.com/logic-operators-in-latex/)
* [KaTeX Support Table](https://katex.org/docs/support_table.html)
* [truth-table-generator](https://pypi.org/project/truth-table-generator/)
* [pipx](https://github.com/pypa/pipx)
* [Sum in LaTeX (Sigma symbol)](https://latex-tutorial.com/sum-latex/)
* [How to write product(Π) and big Pi by prod command in LaTeX?](https://www.physicsread.com/use-of-product-notation-in-latex/)
* [How to denote latex vertical dots(⋮) symbol?](https://www.physicsread.com/latex-vertical-dots-symbol/)
* [Is 0 a Natural Number: A Beginner's Guide](https://www.storyofmathematics.com/is-0-a-natural-number/)
