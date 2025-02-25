import ttg

print(ttg.Truths(
    ['p', 'q', 'r'],
    ['p => (q or r)', '(p = q) or (p => r)'],
    ints=False)
)
