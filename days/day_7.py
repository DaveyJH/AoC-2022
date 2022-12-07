#!/usr/bin/env python

import re
from aoc_data import check_for_data, data_file

DAY = re.search(r"(\d+)\.py", __file__).group(1)
check_for_data()
print(f"Day {DAY}:\n")

with open(data_file()) as f:
    content = f.readlines()
    file_sys = {
        "/": {}
    }
    ls_command = re.compile(r"\$ ls")
    cd_command = re.compile(r"\$ cd (.+)")
    dir_regex = re.compile(r"dir (.+)")
    file_regex = re.compile(r"(\d+) (.+)")
    pd = []
    cd = None
    for line in content:
        keys = [*pd]
        cwd = file_sys
        while keys:
            cwd = cwd[keys.pop(0)]
        if cd_r := cd_command.match(line):
            if cd and cd_r.group(1) != "..": pd.append(cd)
            cd = cd_r.group(1)
            if cd == "..":
                cd = pd.pop(-1)
            pass
        if ls_command.match(line):
            pass
        if dir_r := dir_regex.match(line):
            cwd[cd][dir_r.group(1)] = {}
            pass
        if file_r := file_regex.match(line):
            cwd[cd][file_r.group(2)] = int(file_r.group(1))

    print(file_sys)

    print("  Part 1: ",)

    print("  Part 2: ",)

print()
