#!/usr/bin/env python

import re
from aoc_data import check_for_data, data_file

DAY = re.search(r"(\d+)\.py", __file__).group(1)
check_for_data()
print(f"Day {DAY}:\n")

with open(data_file()) as f:
    content = f.read()

    print("  Part 1: ",)

    print("  Part 2: ",)

print()
