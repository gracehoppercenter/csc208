import ttg

print(ttg.Truths(
    ['p', 'q',],
    ['~p', 'q => p', '~p and (q => p)'],
    ints=False)
)
