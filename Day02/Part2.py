from pathlib import Path

total_score = 0

p = Path(__file__).with_name('Input.txt')
with p.open('r') as f:
    for raw_round in f:
        round = raw_round.strip().split()
        
        match round:
            # Lose
            case ('A', 'X'): total_score += 0 + 3
            case ('B', 'X'): total_score += 0 + 1
            case ('C', 'X'): total_score += 0 + 2
            # Draw
            case ('A', 'Y'): total_score += 3 + 1
            case ('B', 'Y'): total_score += 3 + 2
            case ('C', 'Y'): total_score += 3 + 3
            # Win
            case ('A', 'Z'): total_score += 6 + 2
            case ('B', 'Z'): total_score += 6 + 3
            case ('C', 'Z'): total_score += 6 + 1

print(total_score)