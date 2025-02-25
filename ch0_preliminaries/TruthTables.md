# Truth Tables with Python

I found a package on [PyPI](https://pypi.org/) called
[truth-table-generator](https://pypi.org/project/truth-table-generator/).

To install it on my Debian 12 workstation, I first installed
[pipx](https://github.com/pypa/pipx) with:
```
sudo apt install pipx
```
and than ran:
```
pipx install truth-table-generator
```
This package has a nice cli extension that let me run:
```
ttg_cli.py "['p', 'q']" -p "['p => q', '~p or q']" -i False
```
and see:
```
+-------+-------+----------+-----------+
|   p   |   q   |  p => q  |  ~p or q  |
|-------+-------+----------+-----------|
| True  | True  |   True   |   True    |
| True  | False |  False   |   False   |
| False | True  |   True   |   True    |
| False | False |   True   |   True    |
+-------+-------+----------+-----------+
```
Nice!
