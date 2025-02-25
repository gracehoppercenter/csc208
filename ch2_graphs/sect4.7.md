# Section 4.7: Chapter Summary Exercises


## Exercise 5

Consider the graph $G_1 = (V_1, E_1)$ with $V_1 = \{a, b, c, d, e, f, g\}$ and
$E_1 = \{\{a, b\}, \{a, c\}, \{a, f\}, \{b, g\}, \{c, d\}, \{c, e\}\}$.

### Part (a)

Is the graph $G_1$ isomorphic to $G_2 = (V_2, E_2)$ with
$V_2 = \{t, u, v, w, x, y, z\}$ and
$E_2 = \{\{t, z\}, \{u, v\}, \{u, y\}, \{u, z\}, \{v, w\}, \{v, x\}\}$. If so,
give the isomorphism. If not, explain how you know.

> The following function $f$ defines an isomorphism from $G_1$ to $G_2$:
> ```math
> \begin{array}{l|lllllll}
> x & a & b & c & d & e & f & g \\
> \hline
> f(x) & u & z & v & w & x & y & t \\
> \end{array}
> ```
>
> The following diagrams allow us to visualize this isomorphism.
> ### $G_1$ Diagram
> ```mermaid
> graph TD;
>    a --> f;
>    a --> c;
>    a --> b;
>    c --> e;
>    c --> d;
>    b --> g;
> ```
> ### $G_2$ Diagram
> ```mermaid
> graph TD;
>    u --> y;
>    u --> v;
>    u --> z;
>    v --> x;
>    v --> w;
>    z --> t;
> ```


### Part (b)

Find a graph $G_3$ with 7 vertices and 6 edges which is *not* isomorphic to
$G_1$, or explain why this is not possible.


### Part (c)

Write down the *degree sequence* for the vertices of $G_1$ in decreasing order.


### Part (d)

Find a connected graph $G_4$ with the same degree sequence as $G_1$ which is
*not* isomorphic to it, or explain why this is not possible.

