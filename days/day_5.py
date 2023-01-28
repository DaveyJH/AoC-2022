#!/usr/bin/env python

import re
from aoc_data import check_for_data, data_file, get_day

DAY = get_day()
check_for_data()
print(f"Day {DAY}:\n")

with open(data_file()) as f:
    content = f.readlines()
    CRATE = re.compile(r"   |\[(\w)\] ?")
    NUM_OF_COLS = len(CRATE.findall(content[0]))
    COLS = [[] for _ in range(NUM_OF_COLS)]
    REVISED_COLS = [[] for _ in range(NUM_OF_COLS)]
    for i, line in enumerate(content):
        row = CRATE.findall(line)
        if len(row) != NUM_OF_COLS: break
        for j, crate in enumerate(row):
            if crate:
                COLS[j].append(crate)
                REVISED_COLS[j].append(crate)
    i += 2
    k = i
    MOVEMENT = re.compile(r"move (\d+) from (\d+) to (\d+)")
    while i < len(content):
        count, origin, destination = MOVEMENT.match(content[i]).groups()
        count = int(count)
        while count:
            COLS[int(destination) - 1].insert(0, COLS[int(origin) - 1].pop(0))
            count -= 1
        i += 1
    result = ""
    for col in COLS:
        result += col[0]
    print("  Part 1: ", result)
    while k < len(content):
        count, origin, destination = MOVEMENT.match(content[k]).groups()
        count = int(count)
        REVISED_COLS[int(destination) - 1] = (
            REVISED_COLS[int(origin) - 1][0:count]
            + REVISED_COLS[int(destination) - 1]
        )
        REVISED_COLS[int(origin) - 1] = REVISED_COLS[int(origin) - 1][count:]
        k += 1
    revised_result = ""
    for col in REVISED_COLS:
        revised_result += col[0]
    print("  Part 2: ", revised_result)

print()
