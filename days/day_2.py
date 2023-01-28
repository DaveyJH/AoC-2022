#!/usr/bin/env python

import re
from aoc_data import check_for_data, data_file, get_day

DAY = get_day()
check_for_data()
print(f"Day {DAY}:\n")

with open(data_file()) as f:
    content = f.read()
    INITIAL_SCORES = {
        "A X": 4,
        "B X": 1,
        "C X": 7,
        "A Y": 8,
        "B Y": 5,
        "C Y": 2,
        "A Z": 3,
        "B Z": 9,
        "C Z": 6,
    }
    ROUND = re.compile(r"[ABC] [XYZ]")
    rounds = ROUND.findall(content)
    total = sum(INITIAL_SCORES[r] for r in rounds)
    print("  Part 1: ", total)
    REVISED_SCORES = {
        "A X": 3,
        "B X": 1,
        "C X": 2,
        "A Y": 4,
        "B Y": 5,
        "C Y": 6,
        "A Z": 8,
        "B Z": 9,
        "C Z": 7,
    }
    revised_total = sum(REVISED_SCORES[r] for r in rounds)
    print("  Part 2: ", revised_total)

print()
