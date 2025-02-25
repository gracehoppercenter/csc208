import ttg

print(ttg.Truths(
    ['p', 'q', 'r'],
    ['~p', 'q and r', '~p => (q and r)'],
    ints=False)
)
