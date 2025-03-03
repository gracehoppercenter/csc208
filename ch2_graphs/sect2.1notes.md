# Chapter 2.1: Problems and Definitions

## Graph

A **graph** is an ordered pair $G = (V, E)$ consisting of a nonempty
set $V$ (called the **vertices**) and a set $E$ (called the **edges**) of
two-element subsets of $V$.


## Equal Graphs

Two graphs are **equal** when their sets of vertices, $V$, and edges, $E$, are
both equal.


## Isomorphic Graphs

An **isomorphism** between two graphs $G_1$ and $G_2$ is a
[bijection](https://en.wikipedia.org/wiki/Bijection)
$f: V_1 \rightarrow V_2$ between the vertices of the graphs such that
$\{a, b\}$ is an edge in $G_1$ if and only if $\{f(a), f(b)\}$ is an edge in
$G_2$. Two graphs are **isomorphic** if there is an
[isomorphism](https://en.wikipedia.org/wiki/Isomorphism) between them. In this
case we write $G_1 \cong G_2$.


## Isomorphism Class

A collection of isomorphic graphs is called an **isomorphism class**. One such
well known example of an
[isomorphism class](https://en.wikipedia.org/wiki/Isomorphism_class) is the
[Peterson graph](https://en.wikipedia.org/wiki/Petersen_graph).


## Subgraphs

We say that $G' = (V', E')$ is a **subgraph** of $G = (V, E)$, and write
$G' \subseteq G$, provided $V' \subseteq V$ and $E' \subseteq E$. We say that
$G' = (V', E')$ is an **induced subgraph** of $G = (V, E)$ provided
$V' \subseteq V$ and every edge in $E$ whose vertices are still in $V'$ is
also an edge in $E'$. 


## Other Graph Properties

A **multigraph** is a graph in which multiple edges (also called *parallel
edges*) are permitted between vertices.
The term [multigraph](https://en.wikipedia.org/wiki/Multigraph) is sometimes
used synonymously with the term *pseudograph*, which is a graph that also
permits edges between a vertex and itself (called a *loop* or *buckle*).

A graph is **connected** when there is a path between any vertex in the graph
to any other vertex in the graph.

A graph is **complete** if it contains all possible edges. That is, given
any two vertices in the graph, there is an edge connecting them.  $K_n$ is
the complete graph with $n$ vertices.

The **degree**, $d(v)$ of a vertex $v$ of a graph is the number of edges
emanating from it.

A graph is **bipartite** if the vertices can be divided into two sets,
$A$, and $B$, with no two vertices in $A$ adjacent and no two vertices in
$B$ adjacent. If each vertex in $A$ is adjacent to all the vertices in $B$,
the graph is a **complete bipartite graph**, and gets a special name:
$K_{m, n}$, where $|A| = m$ and $|B| = n$. 


## Handshake Lemma (Lemma 4.1.5)

In any graph the sum of the sum of the degrees of vertices in the graph is
always twice the number of edges.
```math
\sum_{v \in V} d(v) = 2e.
```

The **degree sequence** of a graph is a list of the degree of every vertex in
the graph, usually written in non-increasing order.


## Proposition 4.1.8

In any graph, the number of vertices with odd degree must be even.


## Named Graphs

$K_n$
: The complete graph on $n$ vertices.

$K_{m, n}$
: The complete bipartite graph with sets of $m$ and $n$ vertices.

$C_n$
: The cycle of $n$ vertices.

$P_n$
: The path on $n + 1$ vertices ($n$ edges).

![K5](illustrations/k5.svg)
![K2,3](illustrations/k2_3.svg)
![C6](illustrations/c6.svg)
![P5](illustrations/p5.svg)


## Graph Theory Definitions

**Graph**
: A collection of **vertices**, some of which are connected by **edges**. More
  precisely, a pair of sets $V$ and $E$ where $V$ is a set of vertices
  and $E$ is a set of 2-element subsets of $V$.

**Adjacent**
: Two vertices are **adjacent** if they are connected by an edge. Two edges are
  adjacent if they share a vertex.

**Bipartite graph**
: A graph for which it is possible to divide the vertices into two disjoint
  sets such that there are no edges between any two vertices in the same set.

**Complete bipartite graph**
: A bipartite graph for which every vertex in the first set is adjacent to
  every vertex in the second set.

**Complete graph**
: A graph in which every pair of vertices is adjacent.

**Connected graph**
: A graph is **connected** if there is a path from any vertex to any other
  vertex.

**Chromatic number**
: The minimum number of colors required in a proper vertex coloring of the
  graph.

**Cycle**
: A path that starts and stops at the same vertex, but contains no other
  repeated vertices.

**Degree of a vertex**
: The number of edges incident to a vertex.

**Euler path**
: A walk which uses each edge exactly once.

**Euler circuit**
: An Euler path which starts and stops at the same vertex.

**Multigraph**
: A **multigraph** is just like a graph but can contain multiple edges between
  two vertices as well as between a single vertex and itself (a *loop* or
  *buckle*).

**Path**
: A **path** is a walk that doesn't repeat any vertices (or edges) except
  perhaps the first and last. If a path starts and ends at the same vertex, it
  is called a **cycle**.

**Planar graph**
: A graph which can be drawn in a plane without any edges crossing.

**Subgraph**
: We say that $H$ is a **subgraph** of $G$ if every vertex and edge of $H$ is
  also a vertex or edge of $G$. We say $H$ is an **induced subgraph**
  of $G$ if every vertex of $H$ is a vertex of $G$ and each pair of vertices
  in $H$ are adjacent in $H$ if and only if they are adjacent in $G$.

**Tree**
: A connected graph with no cycles. If we remove the requirement that the
  graph is connected, the graph is called a **forest**.) The vertices in a tree
  with degree 1 are called **leaves**.

**Vertex coloring**
: An assignment of colors to each of the vertices of a graph. A vertex coloring
  is called a **proper coloring** if adjacent vertices are always colored
  differently.

**Walk**
: A sequence of vertices such that consecutive vertices in the sequence are
  adjacent in the graph.  A walk in wich no edge is repeated is called a
  **trail**, and a trail in which no vertex is repeated (except possibily the
  first and last) is called a **path**.
