#!/usr/bin/env python

import re
from aoc_data import check_for_data, data_file, get_day

DAY = get_day()
check_for_data()
print(f"Day {DAY}:\n")


class File:

    def __init__(self, name, size):
        self.name = name
        self.size = int(size)


class Directory:

    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.files: dict[str, File] = {}
        self.dirs: dict[str, Directory] = {}

    def calc_size(self):
        """Returns total size of all decendant files"""
        return (
            sum(f.size for f in self.files.values())
            + sum(d.calc_size() for d in self.dirs.values())
        )


LS_CMD = re.compile(r"\$ ls")
CD_CMD = re.compile(r"\$ cd (.+)")
DIR_REGEX = re.compile(r"dir (.+)")
FILE_REGEX = re.compile(r"(\d+) (.+)")

# part 2 (added after part 1...sort of cheating?)
TOTAL_SPACE = 70000000
SPACE_REQUIRED = 30000000
SPACE_REMAINING = 25874010  # TOTAL_SPACE - root.calc_size()
DIR_SIZE_REQUIRED = SPACE_REQUIRED - SPACE_REMAINING

with open(data_file()) as f:
    content = f.readlines()
    root = Directory("/")  # create root
    cd = root  # start at root
    part_1_size = 0
    part_2_dirs: list[Directory] = []
    for line in content:
        if cd_reg := CD_CMD.match(line):
            if cd_reg.group(1) == "/":
                cd = root  # return to root
            elif (name := cd_reg.group(1)) != "..":
                cd = cd.dirs[name]  # cd to relevant directory
            else:
                if (size := cd.calc_size()) <= 100000:
                    part_1_size += size
                elif cd.calc_size() >= DIR_SIZE_REQUIRED:
                    part_2_dirs.append(cd)
                cd = cd.parent  # `cd ..` to parent
        elif dir_reg := DIR_REGEX.match(line):
            dir = dir_reg.group(1)
            cd.dirs[dir] = Directory(dir, cd)  # add directory as child of cd
        elif file_reg := FILE_REGEX.match(line):
            f_size, f_name = file_reg.group(1, 2)
            cd.files[f_name] = File(f_name, f_size)  # add file w/size to cd
    if (size := cd.calc_size()) <= 100000:  # needed to check final cd
        part_1_size += size

    print("  Part 1: ", part_1_size)
    print("  Part 2: ", min(d.calc_size() for d in part_2_dirs))

print()
