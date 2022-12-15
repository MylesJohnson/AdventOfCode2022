from pathlib import Path
from string import ascii_letters

priorities = {c: i + 1 for i, c in enumerate(ascii_letters)}
total = 0

p = Path(__file__).with_name('Input.txt')
with p.open('r') as f:
    groups = zip(*[iter(f)]*3) # Gets three rucksacks at a time. grouper from https://docs.python.org/3/library/itertools.html#itertools-recipes 
    for group in groups:
        one = set(group[0].strip())
        two = set(group[1].strip())
        three = set(group[2].strip())

        common = next(iter(one & two & three)) # Set intersection
        total += priorities[common]

print(total)