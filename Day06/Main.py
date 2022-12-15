from pathlib import Path

#distict_count = 4 # Part 1
distict_count = 14 # Part 2

p = Path(__file__).with_name('Input.txt')
with p.open('r') as f:
    datastream = f.read()

i = 0

while(len(set(datastream[i:i+distict_count])) != distict_count):
    i += 1

print(i+distict_count)