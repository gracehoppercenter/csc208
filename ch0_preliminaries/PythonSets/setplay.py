from random import randint

s1 = {2 * x for x in range(1, 11)}
s2 = {3 * x for x in range(1, 11)}
s3 = {randint(1, 60) for i in range(10)}
print(f"The union of\n  {s1}\nand\n  {s2}\nis\n  {s1 | s2}")
print(f"The intersection of\n  {s1}\nand\n  {s2}\nis\n  {s1 & s2}")
