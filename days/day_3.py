#!/usr/bin/env python

import re
from aoc_data import check_for_data, data_file, get_day

DAY = get_day()
check_for_data()
print(f"Day {DAY}:\n")

with open(data_file()) as f:
    content = f.read()
    RUCKSACK = re.compile(r"\w+")
    all_rucksacks = RUCKSACK.findall(content)
    items = []
    for rucksack in all_rucksacks:
        first = set(rucksack[0:len(rucksack) // 2])
        second = set(rucksack[len(rucksack) // 2:])
        item_type = list(first & second)
        items.append(
            ord(item_type[0]) - 96 if item_type[0].islower() else
            ord(item_type[0]) - 38
        )
    print("  Part 1: ", sum(items))
    groups = []
    group = []
    for i, rucksack in enumerate(all_rucksacks):
        group.append(rucksack)
        if (i + 1) % 3 == 0:
            groups.append(group)
            group = []
    group_items = []
    for group in groups:
        item_type = list(
            set(group[0])
            & set(group[1])
            & set(group[2])
        )
        group_items.append(
            ord(item_type[0]) - 96 if item_type[0].islower() else
            ord(item_type[0]) - 38
        )
    print("  Part 2: ", sum(group_items))

print()
