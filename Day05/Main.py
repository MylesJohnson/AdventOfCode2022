from pathlib import Path
import re

regex = re.compile(r'move (\d+) from (\d+) to (\d+)')

stacks = [[],[],[],[],[],[],[],[],[]]

p = Path(__file__).with_name('Input.txt')
with p.open('r') as f:
    lines_top, lines_bottom = [l.split('\n') for l in f.read().split('\n\n')]

for line in lines_top:
    for i, crate in enumerate(line[1::4]):
        if crate != ' ' and crate.isalpha():
            stacks[i].insert(0, crate)

for step in lines_bottom:
    move, source, dest = map(int, regex.search(step).groups())
    r = [stacks[source-1].pop() for _ in range(move)]
    stacks[dest-1].extend(r) # part 1
    #stacks[dest-1].extend(reversed(r)) # part 2

print(''.join([stack[-1] if stack else '' for stack in stacks]))