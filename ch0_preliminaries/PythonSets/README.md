# Python Sets

Both **set** and **frozenset** contain collections of distinct
[hashable](https://docs.python.org/3/glossary.html#term-hashable) objects,
with sets mutable and frozensets immutable.


## Set Operations 

| Operation          | Description                                             |
|--------------------|---------------------------------------------------------|
| len(s)             | Return the number of items in s.                        |
| x in s             | True if s contains x, False otherwise.                  |
| s <= o             | True if all elements of s are in o.                     |
| s < o              | True if s is a *proper subset* of s.                    |
| s >= o             | True if all elements of o are in s.                     |
| s > o              | True if s is a *proper superset* of o.                  |
| s \| o             | Union of s and o.                                       |
| s & o              | Intersection of s and o.                                |
| s - o              | Elements in s that are *not* in o.                      |
| s ^ o              | Elements in s *or* o, but not in both.                  |
| s.copy()           | Return a shallow copy of s.                             |


## Additional Mutable Set Operations 

| Operation          | Description                                             |
|--------------------|---------------------------------------------------------|
| s |= o             | Add elements from set o to set s.                       |
| s &= o             | Update s, keeping only elements in o.                   |
| s -= o             | Update s, removing any elements found in o.             |
| s ^= o             | Update s, keeping elements in s or o, but not both.     |
| s.add(e)           | Add element e to set s.                                 |
| s.remove(e)        | Remove element e from set s.                            |
| s.disgard(e)       | Remove element e from set s if it is present.           |
| s.pop()            | Remove and return arbitrary element from non-empty s.   |
| s.clear()          | Remove all elements from set s.                         |


## Resources

* [Python Tutorial: Sets](https://docs.python.org/3/tutorial/datastructures.html#sets)
* [Python Library Reference: Sets](https://docs.python.org/3/library/stdtypes.html#set)
