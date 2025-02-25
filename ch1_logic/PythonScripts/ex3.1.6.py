import ttg

print(ttg.Truths(
    ['p', 'q',],
    ['~(p => q)', '(p and ~q)'],
    ints=False)
)
