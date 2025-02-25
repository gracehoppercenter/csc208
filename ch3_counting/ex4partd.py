hexdigits = "0123456789ABCDEF"
setA = set()
for d1 in "ABCDEF":
    for d2 in hexdigits:
        for d3 in hexdigits:
            setA.add(f"{d1}{d2}{d3}")
print(f"\nSet A has {len(setA)} hex numbers.")

setB = set()
for d1 in hexdigits: 
    for d2 in hexdigits:
        for d3 in "0123456789":
            setB.add(f"{d1}{d2}{d3}")
print(f"Set B has {len(setB)} hex numbers.")
print(f"The intersection of sets A and B has {len(setA & setB)} hex numbers.")
