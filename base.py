#!/usr/bin/env python3

import sys

def part_1(matrix):
    pass

def part_2(matrix):
    pass

def main():
    if len(sys.argv) < 2:
        print("missing required input file", file=sys.stderr)
        sys.exit(1)

    with open(sys.argv[1]) as f:
        lines = f.readlines()
        lines[-1] += "\n"

    print(f"#1: {part_1(lines)}")
    print(f"#2: {part_2(lines)}")

if __name__ == "__main__":
    main()