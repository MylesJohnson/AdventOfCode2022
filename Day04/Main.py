from pathlib import Path

count_part_one = 0
count_part_two = 0

p = Path(__file__).with_name('Input.txt')
with p.open('r') as f:
    for pair in f:
        elf_one, elf_two = pair.strip().split(',')

        elf_one_start, elf_one_stop = map(int, elf_one.split('-'))
        elf_one_set = set(range(elf_one_start, elf_one_stop + 1)) # plus one because range is exclusive

        elf_two_start, elf_two_stop = map(int, elf_two.split('-'))
        elf_two_set = set(range(elf_two_start, elf_two_stop + 1)) # plus one because range is exclusive

        # The performance of converting to sets is much worse than just integer comparisons, but I think its cleaner code
        count_part_one += elf_one_set.issubset(elf_two_set) or elf_two_set.issubset(elf_one_set)
        count_part_two += len(elf_one_set & elf_two_set) > 0

print(f"Part One: {count_part_one}")
print(f"Part Two: {count_part_two}")