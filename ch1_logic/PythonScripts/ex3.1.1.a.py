import ttg

print(ttg.Truths(
    ['p', 'q',],
    ['~p and ~q', 'p or q  => q', '(~p and ~q) or q'],
    ints=False)
)
