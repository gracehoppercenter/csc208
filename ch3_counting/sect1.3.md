# Section 1.3: Combinations and Permutations Exercises 


## Exercise 1

> A pizza parlor offers 10 toppings.

### Part (a)

> How many 3-topping pizzas could they put on their menu?

There are ${10\choose 3} = 120$ possible 3-topping pizzas.

### Part (b)

> How many total pizzas are possible, with between zero and ten toppings?

The total possible pizzas equals the sum of the values in the row 10 (starting
at 0), which is $2 \cdot (1 + 10 + 45 + 120 + 210) + 252 = 1024$ possible
pizza. We can also derive this result using the multiplicative principle,
with $2^10 = 1024$. 

### Part (c)

> The pizza parlor will list the 10 toppings in equal-sized columns on their
> menu. How many ways can they arrange the toppings in the left column?

5 of the 10 toppings will be listed on the left column of the menu, so we
are interested in the value of 10-permutations of 5 elements, or
$P(10, 5) = \frac{10!}{5!} = 10 \cdot 9 \cdot 8 \cdot 7 \cdot 6 = 30240$
possible arrangements of 5 of the 10 toppings on the left menu column. 


## Exercise 2

> A combination lock consists of a dial with 40 numbers on it. To open the
> lock, you turn the dial to the right until you reach a first number, then to
> the left until you get to second number, then to the right again to the third
> number. The numbers must be distinct. How many different combinations are
> possible?

We are looking for $P(40, 3) = 40 \cdot 39 \cdot 38 = 59280$ possible
combinations.


## Exercise 3

> Using the digits 2 through 8, find the number of different 5-digit numbers
> such that:

### Part (a)

> Digits can be used more than once.

This is a repeat of solution to exercise 1.1.12.a. Here there are 7 different
digits instead of 8, giving us $7^5 = 16807$ possible 5-digit numbers composed
of them.

### Part (b)

> Digits cannot be repeated, but can come in any order.

In the same vain as in 1.1.12.b, we have
$7 \cdot 6 \cdot 5 \cdot 4 \cdot 3 = 2520$ different 5-digits numbers that can
be formed from the digits 2 through 8 with no repeated digits.

### Part (c)

> Digits cannot be repeated and must be written in increasing order.

There are ${7\choose 5} = \frac{7!}{2!5!} = 21$ different ways to choose
5 digits from 7, and here only a single way to arrange them (in increasing
order) once they are choosed, so there are 21 such numbers in total.


### Part (d)

> Which of the above counting questions is a combination and which is a
> permutation? Explain why this makes sense. 


## Exercise 4

> In an attempt to clean up your room, you have purchased a new floating shelf
> to put some of your 17 books you have stacked in a corner. These books are
> all by different authors. The new book shelf is large enough to hold 10 of
> the books.

### Part (a)

> How many ways can you select and arrange 10 of the 17 books on the shelf?
> Notice that here we will allow the books to end up in any order. Explain.



### Part (b)

> How many ways can you arrange 10 of the 17 books on the shelf if you insist
> they must be arranged alphabetically by author? Explain.


