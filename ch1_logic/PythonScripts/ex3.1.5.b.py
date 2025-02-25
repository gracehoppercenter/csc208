import ttg

print(ttg.Truths(
    ['p', 's', 'q', 'r'],
    ['(p xor s) and (s => q) and ((p or q) => r)'],
    ints=False)
)
