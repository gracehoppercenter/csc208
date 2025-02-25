# Discrete Math Sequences Test


1. Write both the recursive definition and the closed formula for the sequence
   of odd numbers, $(a_n)_{n \ge 1} = 1, 3, 5, 7, 9,...$. Then write the
   recursive definition for the sequence of partial sums,
   ${(T_n)}_{n \ge 0}$ with $T_0 = 0$, of the elements of $({a_n})$. Finally,
   list the first five elements of $T_n$.

   > The recursive definition for this sequence is $a_n = a_{n-1} + 2$ with
   > $a_1 = 1$. The closed formula is $a_n = 2n - 1$. The sequence of partial
   > sums of the terms of $(a_n)$ is definted by $T_n = \sum^n_{i = 0} a_i$. As
   > always, the recursive defintion for the sequence of partial sums is
   > $T_n = T_{n-1} + a_n$, with $T_0 = 0$. Given $({a_n})$ 's closed formula,
   > this can be writted as $T_n = T_{n-1} + 2n - 1$. The first five elements
   > of this sequence are 1, 4, 9, 16, and 25.


2. Find the closed formula for the sequence of partial sums, $(T_n)_{n \ge 0}$,
   of the elements in the sequence $(a_n)_{n \ge 1} = 2, 6, 10, 14, 18,...$.

   > The differences between elements of $(a_n)$ is constant (4), so it is an
   > arithmetic sequence and we can use the *reverse and add* approach to find
   > the closed formula for its sequence of partial sums.  Let's write out the
   > first few elements of the sequence of partial sums.
   > ```math
   > \begin{align*}
   > T_1 &= 2 \\
   > T_2 &= 2 + 6 &= 8 \\
   > T_3 &= 2 + 6 + 10 &= 18 \\
   > T_4 &= 2 + 6 + 10 + 14 &= 32 \\
   > T_5 &= 2 + 6 + 10 + 14 + 18 &= 50 \\
   > \vdots \\
   > T_n &= 2 + 6 + 10 + ... + (4n + 2) 
   > \end{align*}
   > ```
   > Now let's reverse and add.
   > ```math
   > \begin{array}{cccccccccccc}
   >   & T_n & = & 2 & + & 6 & + & ... & + & {4n - 6} & + & {4n - 2} \\
   > + & T_n & = & {4n - 2} & + & {4n - 6} & + & ... & + & 6 & + & 2 \\
   > \hline
   >   & 2T_n & = & 4n & + & 4n & + & ... & + & 4n & + & 4n \\
   > \end{array}
   > ```
   > There are $n$ terms, so $2T_n = n(4n) = 4n^2$, and $T_n = 2n^2$.


3. Find the sum of all the terms in the sequence $1, 7, 13, 19, ..., 6n + 1$.

   > As in the previous problem, we can reverse and add. Let's again write out
   > the first few elements of the sequence of partial sums to make it easier
   > to check our result.
   > ```math
   > \begin{align*}
   > T_0 &= 1 \\
   > T_1 &= 1 + 7 &= 8 \\
   > T_2 &= 1 + 7 + 13 &= 21 \\
   > T_3 &= 1 + 7 + 13 + 19 &= 40 \\
   > T_4 &= 1 + 7 + 13 + 19 + 25 &= 65 \\
   > \vdots \\
   > T_n &= 1 + 7 + 13 + ... + (6n + 1) 
   > \end{align*}
   > ```
   > Now reverse and add.
   > ```math
   > \begin{array}{cccccccccccc}
   >   & T_n & = & 1 & + & 7 & + & ... & + & {6n - 5} & + & {6n + 1} \\
   > + & T_n & = & {6n + 1} & + & {6n - 5} & + & ... & + & 7 & + & 1 \\
   > \hline
   >   & 2T_n & = & {6n + 2} & + & {6n + 2} & + & ... & + & {6n + 2} & +
   > & {6n + 2} \\
   > \end{array}
   > ```
   > We started counting from 0, so there are $n + 1$ terms, and
   > $2T_n = (n + 1)(6n + 2)$, and $T_n = 3n^2 + 4n + 1$. We can confirm
   > that $T_3 = 3 \cdot 3^2 + 4 \cdot 3 + 1 = 27 + 12 + 1 = 40$ and
   > $T_4 = 3 \cdot 4^2 + 4 \cdot 4 + 1 = 48 + 16 + 1 = 65$.


4. Use polynomial fitting to find the formula for the $n\text{th}$ term of
   the sequence which starts with $1, 2, 8, 19, 35, 56, ...$.

   > The sequence of first differences is $1, 6, 11, 16, 21,...$.  The
   > sequence of second differences is constant (5), so the original
   > sequence is $\Delta^2\text{-constant}$ and its closed formula will be
   > of the form: $s_n = an^2 + bn + c$.
   > $s_0 = 1 = a \cdot 0^2 + b \cdot 0 + c = c$.
   > $s_1 = 2 = a + b + 1$, so $a + b = 1$.
   > $s_2 = 8 = a \cdot 2^2 + b \cdot 2 + 1$, so $4a + 2b = 7$.
   > Substituting $b = 1 - a$ from $s_1$ into $s_2$ gives us
   > $4a + 2(1 - a) = 7$, which simplifies to $a = \frac{5}{2}$. Substituting
   > this value back into $s_1$ yields $b = \frac{-3}{2}$, giving a closed
   > formula for the $n\text{th}$ term of this sequence:
   > ```math
   > s_n = \frac{5}{2}n^2 - \frac{3}{2}n + 1
   > ```
   > (*Note*: See YouTube video,
   > [Find a Closed Formula for a Sequence Using Polynomial Fitting](https://www.youtube.com/watch?v=vbrAuNGPB1Q)
   > by our textbook author for a step-by-step presentation of this problem).


5. Solve the recurrence relation $a_n = 6a_{n-1} - 9a_{n-2}$ with initial
   conditions $a_0 = 1$ and $a_1 = 4$.

   > The characteristic polynomial is $x^2 - 6x + 9$. We solve the
   > characteristic equation $x^2 - 6x + 9 = 0$ by factoring, yielding
   > $(x - 3)^2 = 0$ and telling us $x = 3$ is the only root and thus
   > the solution to the recurrance relation has the form
   > $a_n = a3^n bn3^n$ for some constants $a$ and $b$. Using the initial
   > conditions, we get:
   > ```math
   > \begin{align*}
   > a_0 &= 1 &= a3^0 b \cdot 0 \cdot 3^0 &= a \\
   > a_1 &= 4 &= a3^1 b \cdot 1 \cdot 3^1 &= 3a + 3b
   > \end{align*}
   > ```
   > Thus the solution to the recurrance relation is
   > ```math
   > a_n = 3^n + \frac{1}{3}n3^n
   > ```


6. Prove that $2^n < n!$ for all $n \ge 4$.

   > Let $P(n)$ be the statement $2^n < n!$. We want to show $P(n)$ is true
   > for all $n \ge 4$. $P(4)$ is the statement $2^4 < 4!$, which is true
   > (since 16 is less than 24). Now assume the *inductive hypothesis*,
   > $P(k)$, that $2^k < k!$ for some $k \ge 4$. We need to show that
   > $2^{k+1} < (k + 1)!$.
   > ```math
   > \begin{array}{lll}
   > (1) & 2 < k + 1 & \text{Inductive hypothesis that } k \ge 4 \\
   > (2) & 2^k < k! & \text{Induction hypothesis} \\
   > (3) & 2 \cdot 2^k < 2 \cdot k! & \text{(2), Multiplicative property of inequality} \\
   > (4) & 2^{k + 1} < 2 \cdot k! & \text{(3), Defintion of exponent} \\
   > (5) & 2 \cdot k! < (k + 1) \cdot k! & \text{(1), Multiplicative property of inequality} \\
   > (6) & 2 \cdot k! < (k + 1)! & \text{(5), Defintion of factorial} \\
   > (7) & 2^{k + 1} < (k + 1)! & \text{(4), (6), Transitive property of inequality} \\
   > \end{array}
   > ```
   > Therefore, by the principle of mathematical induction, $2^n < n!$ for
   > all $n \ge 4$.
