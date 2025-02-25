import ttg

print(ttg.Truths(
    ['r', 'w', 's'],
    ['(r and w) => s', '~((r and w) => s)'],
    ints=False)
)
print(ttg.Truths(
    ['r', 'w', 's'],
    ['~((r and w) => s)', 'r and w and ~s'],
    ints=False)
)
print(ttg.Truths(
    ['r', 'w', 's'],
    ['(r and w) => s', '~s => ~r or ~w'],
    ints=False)
)
print(ttg.Truths(
    ['r', 'w', 's'],
    ['~((r and w) => s)', '~(r and w) => ~s'],
    ints=False)
)
print(ttg.Truths(
    ['r', 'w', 's'],
    ['~((r and w) => s)', '~(r and w) => ~s'],
    ints=False)
)

