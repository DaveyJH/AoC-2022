#!/usr/bin/env python

import re
from aoc_data import check_for_data, data_file, get_day

DAY = get_day()
check_for_data()
print(f"Day {DAY}:\n")

with open(data_file()) as f:
    content = f.read()
    ELF_INVENTORY = re.compile(r"((?:\d+\n)+)")
    SINGLE_ITEM = re.compile(r"\d+")
    all_elves = ELF_INVENTORY.findall(content)
    totals = [
        sum(
            int(item) for item in SINGLE_ITEM.findall(elf)
        ) for elf in all_elves
    ]
    print("  Part 1: ", max(totals))
    print("  Part 2: ", sum(sorted(totals, reverse=True)[0:3]))

print()
