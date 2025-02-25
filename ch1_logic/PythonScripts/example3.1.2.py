import ttg

print(ttg.Truths(
    ['p', 'q', 'r'],
    ['p => q', 'q => r', '(p => q) or (q => r)'],
    ints=False)
)
