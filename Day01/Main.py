from pathlib import Path

p = Path(__file__).with_name('Input.txt')
with p.open('r') as f:
    inputs = f.read()

calories = [sum(map(int, elf.split('\n'))) for elf in inputs.split('\n\n')]

print(f"Answer One: {max(calories)}")
print(f"Answer two: {sum(sorted(calories)[-3:])}")