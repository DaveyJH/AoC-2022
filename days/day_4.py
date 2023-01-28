#!/usr/bin/env python

import re
from aoc_data import check_for_data, data_file, get_day

DAY = get_day()
check_for_data()
print(f"Day {DAY}:\n")

with open(data_file()) as f:
    content = f.readlines()
    FIRST = re.compile(r"^(\d+-\d+)")
    SECOND = re.compile(r",(\d+-\d+)$")
    NUMS = re.compile(r"(\d+)-(\d+)")
    total = 0
    revised_total = 0
    for line in content:
        first = FIRST.match(line).group(1)
        second = SECOND.search(line).group(1)
        first_low, first_high = NUMS.match(first).groups()
        second_low, second_high = NUMS.match(second).groups()
        if (
            (
                int(first_low) <= int(second_low)
                and int(first_high) >= int(second_high)
            )
            or (
                int(second_low) <= int(first_low)
                and int(second_high) >= int(first_high)
            )
        ):
            total += 1
        if (
            (
                int(first_low) <= int(second_low)
                and int(first_high) >= int(second_low)
            )
            or (
                int(second_low) <= int(first_low)
                and int(second_high) >= int(first_low)
            )
        ):
            revised_total += 1
    print("  Part 1: ", total)
    print("  Part 2: ", revised_total)

print()
