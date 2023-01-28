#!/usr/bin/env python

import re
from aoc_data import check_for_data, data_file, get_day

DAY = get_day()
check_for_data()
print(f"Day {DAY}:\n")

with open(data_file()) as f:
    content = f.read()
    marker_count = 4
    while True:
        if len(set(content[marker_count - 4:marker_count])) == 4:
            break
        marker_count += 1
    print("  Part 1: ", marker_count)
    message_count = 14
    while True:
        if len(set(content[message_count - 14:message_count])) == 14:
            break
        message_count += 1
    print("  Part 2: ", message_count)

print()
