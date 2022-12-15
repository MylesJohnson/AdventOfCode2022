from pathlib import Path
from string import ascii_letters

priorities = {c: i + 1 for i, c in enumerate(ascii_letters)}
total = 0

p = Path(__file__).with_name('Input.txt')
with p.open('r') as f:
    for rucksack in f:
        halfway = len(rucksack)//2
        compartment_one = rucksack[0:halfway]
        compartment_two = rucksack[halfway:-1] # -1 so we don't get the newline

        common = next(iter(set(compartment_one) & set(compartment_two))) # Set intersection
        total += priorities[common]

print(total)