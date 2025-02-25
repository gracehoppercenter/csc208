# Section 1.2: Binomial Coefficients Exercises 


## Exercise 1

> Let $S = \{1, 2, 3, 4, 5, 6\}$

### Part (a)

> How many subsets are there total?

Using the multiplicative principle, there are $2^6 = 64$ total subsets.

### Part (b)

> How many subsets have $\{2, 3, 5\}$ as a subset?

We want to count the number of subsets in the power set of the remaining
elements in $S$, $|\mathcal{P}(\{1, 4, 6\})|$, since the union of
$\{2, 3, 5\}$ with each of these will be the set of all subsets of $S$
containing $\{2, 3, 5\}$. There are $2^3 = 8$ of these, so there are 8
subsets of $S$ containing $\{2, 3, 5\}$.

### Part (c)

> How many subsets contain at least one odd number? 

It will be easier to answer this question by counting the number of subsets
that do not contain any odd numbers and then substract this from the total
subsets of $S$. $|\mathcal{P}(\{2, 4, 6\})| = 2^3 = 8$, so there are 8 subsets
of $S$ that do not contain an odd number, leaving $64 - 8 = 56$ subsets that
contain at least one odd number.

### Part (d)

> How many subsets contain exactly one even number? 

$|\mathcal{P}(\{1, 3, 5\})| = 2^3 = 8$, so there are 8 subsets of $S$
containing only odd numbers. The union of each of these subsets with the
set containing exactly one element from $\{2, 4, 6\}$ will yield all of the
subsets of $S$ containing exactly one even number. There are
$3 \cdot 8 = 24$ of these.


## Exercise 2

> Let $S = \{1, 2, 3, 4, 5, 6\}$

### Part (a)

> How many subsets are there of cardinality 4?

The answer to this question is the same as the number of bit strings of
length 6 and weight 4, or $|B^6_4|$. A quick peek at Pascal's triangle reveals
that value to be 15.

### Part (b)

> How many subsets of cardinality 4 have $\{2, 3, 5\}$ as a subset?

Since we are specifying three of the four elements in the desired subsets,
we can only choose one additional element from the remaining $\{1, 4, 6\}$,
giving us 3 possible subsets of cardinality 4 containing $\{2, 3, 5\}$.

### Part (c)

> How many subsets of cardinality 4 contain at least one odd number?

We know from part (a) that there are 15 total subsets of $S$ with cardinality
of 4. Since there are only 3 odd elements in $S$, *all* of these have at least
one odd element, so their are 15 subsets of $S$ of cardinality 4 with at least
one odd number.

### Part (d)

> How many subsets of cardinality 4 contain exactly one even number?

The only way for a subset of $S$ to have a cardinality of 4 with exactly one
even number would be for it to also include all three of the odd members of
$S$, which can be done in exactly 3 ways.

## Exercise 3

> Let $A = \{1, 2, 3, 4, ..., 9\}$

### Part (a)

> How many subsets of $A$ are there? 

We are looking for $|\mathcal{P}(A)|$.

### Part (b)

> How many subsets of $A$ contain exactly 5 elements? 

### Part (c)

> How many subsets of $A$ contain only even numbers? 

### Part (d)

> How many subsets of $A$ contain an even number of elements? 

