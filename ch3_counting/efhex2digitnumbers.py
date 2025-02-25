import itertools

last2 = set('EF')
hexdigits = set('0123456789ABCDEF')
pairs = []

for e in itertools.product(last2, hexdigits):
    pairs.append(e)

print(f"\nThere are {len(pairs)} 2-digit hex numbers starting with E or F.")
#print(pairs)

# List the using a nested loop
nums = []
for d1 in "EF":
    for d2 in "0123456789ABCDEF":
        nums.append(f"{d1}{d2}")
print(', '.join(nums))
