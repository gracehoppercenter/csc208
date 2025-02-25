# Section 1.1: Additive and Multiplicative Principles Exercises


## Exercise 1

> Your wardrobe consists of 5 shirts, 3 pairs of pants, and 17 bow ties. How
> many different outfits can you make?

```python
print(5 * 3 * 17)
```


## Exercise 2

> For your college interview, you must wear a tie. You own 3 regular (boring)
> ties and 5 (cool) bow ties.

### Part (a)

> How many choices do you have for your neck-wear?
```python
print(3 + 5)
```
or 8 choices.

### Part (b)

> You realize that the interview is for clown college, so you should probably
> wear both a regular tie and a bow tie. How many choices do you have now?

```python
print(3 * 5)
```
or 15 choices.

### Part (c)

> For the rest of your outfit, you have 5 shirts, 4 skirts, 3 pants, and 7
> dresses. You want to select either a shirt to wear with a skirt or pants, or
> just a dress. How many outfits do you have to choose from?

If I go with the shirt and skirt or pants, I'll have
```python
print(5 * (4 + 3))
```
or 35 choices, each of which is paired with the ties, for a total of
```python
print(3 * 5) * (5 * (4 + 3)))
```
or 525 outfits.

Opting for a dress gives me
```python
print((3 * 5) * 7)
```
or 105 additional options, for a total of
```python
print(((3 * 5) * (5 * (4 + 3))) + ((3 * 5) * 7))
```
or 630 total different combination of things I could wear to the interview.

If the tie combo and "rest of outfit" are not being considered together, I
would have just
```python
print(5 * (4 + 3) + 7)
```
or 42 outfits.


## Exercise 3

> Your Blu-ray collection consists of 9 comedies and 7 horror movies. Give an
> example of a question for which the answer is:

### Part (a)

> 16

You want to watch a movie from your Blu-ray collection tonight. How many
choices do you have?

### Part (b)

> 63

You are inviting friends over for a "Laugh until you screem" double feature
movie festival, where you will show first a comedy and then a horror movie
from your Blu-ray collection. How many total ways can you pair them?


## Exercise 4

### Part (a)

> How many 2-digit hexadecimals are there in which the first digit is E or F?

The following little Python program will count these for us:
```python
import itertools

last2 = set('EF')
hexdigits = set('0123456789ABCDEF')
pairs = []

for e in itertools.product(last2, hexdigits):
    pairs.append(e)

print(f"\nThere are {len(pairs)} 2-digit hex numbers starting with E or F.")
```

Using an argument similar to that presented in *Example 1.1.1*, we count the
number of two digit hex numbers that start with `E` and get 16 (one for each
hex digit). There are likewise 16 hex numbers that start with `F`, so the
total number of hex numbers that start with either `E` or `F` is 16 + 16 = 32.

### Part (b)

The following will list them using nested for loops:
```python
nums = []
for d1 in "EF":
    for d2 in "0123456789ABCDEF":
        nums.append(f"{d1}{d2}")
print(', '.join(nums))
```
Here it is easier to see the multiplicative principle at work. Each two digit
hex number starting with `E` or `F` is formed by first choicing either `E` or
`F`, which can be done two ways, and then choosing the second digit, which
can be done 16 ways, giving $2 \cdot 16 = 32$.

### Part (c)

Choosing the first digit in A-F can occur 6 ways. Choosing the middle digit as
any hex digits can happen 16 ways, and choosing the last digit in 0-9 can
happen 10 ways. So the total number of 3-digit hex numbers that start with
A-F and end with 0-9 is $6 \cdot 16 \cdot 10 = 960$.

### Part (d)

To count the number of 3-digit hex numbers that begin with A-F *or* end with
0-9, let's let $A$ be the set of all 3-digit hex numbers that start with A-F,
and $B$ be the set of all 3-digit hex numbers that end with 0-9.  We are
looking for the cardinality of these two sets, which is given by
$|A \cup B| = |A| + |B| - |A \cap B|$. There are
$6 \cdot 16 \cdot 16 = 1536$ number in set $A$,
$16 \cdot 16 \cdot 10 = 2560$ numbers in set $B$. From part c we know that
$|A \cap B|$ contains 960 numbers, so the count we are looking for is
$1536 + 2560 - 960 = 3136$.

Let's confirm this with Python:
```python
hexdigits = "0123456789ABCDEF"
setA = set()
for d1 in "ABCDEF":
    for d2 in hexdigits:
        for d3 in hexdigits:
            setA.add(f"{d1}{d2}{d3}")
print(f"\nSet A has {len(setA)} hex numbers.")

setB = set()
for d1 in hexdigits: 
    for d2 in hexdigits:
        for d3 in "0123456789":
            setB.add(f"{d1}{d2}{d3}")
print(f"Set B has {len(setB)} hex numbers.")
print(f"The intersection of sets A and B has {len(setA & setB)} hex numbers.")
```


## Exercise 5

> Suppose you have sets $A$ and $B$ with $|A| = 10$ and $|B| = 15$.

### Part (a)

> What is the largest possible value for $|A \cap B|$?

The largest possible value for $|A \cap B|$ is 10, which will be the value
if $A \subseteq B$.

### Part (b)

> What is the smallest possible value for $|A \cap B|$?

If $A$ and $B$ are disjoint sets, their intersection will be the empty set,
and $|A \cap B|$ will be $0$.

### Part (c)

> What are the possible value for $|A \cup B|$?

$|A \cup B|$ can range from $15$ (when $A \subseteq B$) to $25$ (when
$|A \cap B| = 0$).


## Exercise 6

> If $|A| = 8$ and $|B| = 5$, what is $|A \cup B| + |A \cap B|$?

Using the rule for the cardinality of the union of 2 sets, we have
$|A \cup B| = |A| + |B| - |A \cap B|$. Substituting the right hand side
into the expression we are here evaluating, and we get
$|A| + |B| - |A \cap B| + |A \cap B|$, which is $|A| + |B|$, or $13$.


## Exercise 7

> A group of college students were asked about their TV watching habits. Of
> those surveyed, 28 students watch *The Walking Dead*, 19 watch
> *The Blacklist* , and 24 watch *Game of Thrones*. Additionally, 16 watch
> The Walking Dead and The Blacklist, 14 watch The Walking Dead and Game of
> Thrones, and 10 watch The Blacklist and Game of Thrones. There are 8 students 
> who watch all three shows. How many students surveyed watched at least one of
> the shows?

Let's define $W$, $B$, and $G$ as the sets of students who watch
*The Walking Dead*, *The Blacklist*, and *Game of Thrones* respectively.
We are looking for $|W \cup B \cup G|$, which we know from the cardinality
rule for the union of 3 sets is
$|W| + |B| + |G| - |W \cap B| - |W \cap G| - |B \cap G| + |W \cap B \cap G|$
or $28 + 19 + 24 - 16 - 14 - 10 + 8 = 39$ students who watch at least one
of the three shows.


## Exercise 8

> In a recent survey, 30 students reported whether they liked their potatoes
> Mashed, French-fried, or Twice-baked. 15 liked them mashed, 20 liked French
> fries, and 9 liked twice baked potatoes. Additionally, 12 students liked
> both mashed and fried potatoes, 5 liked French fries and twice baked
> potatoes, 6 liked mashed and baked, and 3 liked all three styles. How many
> students hate potatoes? Explain why your answer is correct.

Let's define $S$ as the set of all students reporting, and $M$, $F$, and $T$ 
as the students who like mashed, french-fried, and twice-baked potatoes
respectively. By "students who hate potatoes", we will take it to mean those
students who are not in the set $M \cup F \cup T$. We can calculate the number
of students in this set with:
```math
|S| - (|M| + |F| + |T| - |M \cap F| - |M \cap T| - |F \cap T| +
|M \cap F \cap T|)
```
or $30 - (15 + 20 + 9 - 12 - 5 - 6 + 3) = 6$ students who "hate potatoes.


## Exercise 9

> For how many $n \in {1, 2, ..., 500}$ is $n$ a multiple of one or more of
> 5, 6, or 7?

We are looking for
```math
|A \cup B \cup C| = |A| + |B| + |C| - |A \cap B| - |A \cap C| - |B \cap C| +
|A \cap B \cap C|
```
where $A$, $B$, and $C$ are the set of positive multiples of $5$, $6$, and $7$
less than $500$ respectively. Python can help us here.
```python
A = {n * 5 for n in range(1, 500 // 5 + 1)}
B = {n * 6 for n in range(1, 500 // 6 + 1)}
C = {n * 7 for n in range(1, 500 // 7 + 1)}
print(f"|A ∪ B ∪ C| is {len(A | B | C)}")
```
Giving a result of 215 positive multiples of 5, 6 or 7 in the set of positive
numbers between 1 and 500.

We can calculate this mathematically using the right-hand side of the
equation. $|A|$ is ``500 // 5`` or 100. $|B|$ is ``500 // 6`` or 83, and
$|C|$ is ``500 // 7`` or 71. $|A \cap B|$ is ``500 // 30`` (``5 * 6``) or 16,
$|A \cap C|$ is ``500 // 35`` or 14, and $|B \cap C|$ is ``500 // 42`` or 11.
Finally $|A \cap B \cap C|$ is ``500 // 210`` or 2. Using these values, we
have $100 + 83 + 71 - 16 - 14 - 11 + 2 = 215$, confirming our Python result.


## Exercise 10

> How many positive integers less than 1000 are multiples of 3, 5, or 7?
> Explain your answer using the Principle of Inclusion / Exclusion.

The positive integers less than 1000 that are multiples of 3, 5, or 7 is the
union of three sets: the set of all multiples of 3 less than 1000, the set of
all multiples of 5 less than 1000, and the set of all multiples of 7 less than
1000. If we name these sets $A$, $B$, and $C$ respectively, then the
cardinality rule for the union of three sets tells us that:
```math
|A \cup B \cup C| = |A| + |B| + |C| - |A \cap B| - |A \cap C| - |B \cap C| +
|A \cap B \cap C|
```
We can let Python do the counting for us:
```python
A = {n * 3 for n in range(1, 1000 // 3)}
B = {n * 5 for n in range(1, 1000 // 5)}
C = {n * 7 for n in range(1, 1000 // 7)}
print(f"|A ∪ B ∪ C| is {len(A | B | C)}")
```
and see that the number of positive integers less than 1000 that are multiples
of 3, 5, or 7 is 540. We could calculate this ourselves using the same process
we used in the previous exercise.


## Exercise 11

> Let $A$, $B$, and $C$ be sets.

### Part (a)

> Find $|(A \cup C) \setminus B|$ provided $|A| = 50$, $|B| = 45$, $|C| = 40$,
> $|A \cap B| = 20$, $|A \cap C| = 15$, $|B \cap C| = 23$, and
> $|A \cap B \cap C| = 12$.

Let's start by finding $|A \cup C|$, which by the rule for the cardinality of
the union of 2 sets is $|A| + |B| - |A \cap B| = 50 + 45 - 20 = 75$. 

### Part (b)

> Describe a set in terms of $A$, $B$, and $C$ with cardinality 26.


## Exercise 12

> Consider all 5 letter strings made from the letters a through h.

### Part (a)

> How many of these strings are there in total?

There are 8 letters from a to h. Since our 5 letter string can be any 
combination of these there are $8^5 = 32768$ possible 5 letter strings with
any combination of a through h.

### Part (b)

> How many of these strings contain no repeated letters?

If repeats are not permitted, than there are 8 ways to choose the first
letter, 7 ways to choose second, ..., and 
$8 \cdot 7 \cdot 6 \cdot 5 \cdot 4 = 6720$ 5 letter strings with a through h
containing no repeats.

### Part (c)

> How many of these strings start with the substring "aha"? 

Here we just need to count the number of strings of length 2 that can be made
with the letters a through 8, which is $8^2 = 64$.

### Part (d)

> How many of these strings either start with "aha" or end with "bah" or both?

Since the third letter in the string cannot be both "a" and "b", none of them
start with "aha" and end with "bah".  From part c we have 64 that start with
"aha", and by similar reasoning we have 64 that end with "bah", for a total
of 128 that either start with "aha" or end with "bah".

### Part (e)

> How many of the strings containing no repeats also do not contain the
> substring "bad"?

From part b we know we have 6720 5 letter strings with a through h containing
no repeats. Let's count the ones that contain the substring "bad" and subtract
that number from the total. How many start with "bad"? That would be the
number of strings of length 2 that can be formed from the letters in "cefgh"
with no repeats, or $5 \cdot 4 = 20$ of these. Likewise there are 20 with
"bad" in the middle, and 20 more with "bad" at the end. Removing these 60
strings from the 6720 we started with leaves 6660 strings with no repeats
and no "bad".
