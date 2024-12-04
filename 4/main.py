#!/usr/bin/env python3

import sys

def _search_word(word, matrix, x, y, direction):
    if len(word) == 0:
        return 1

    if x < 0 or y < 0:
        return 0

    if y >= len(matrix) or x >= len(matrix[y]):
        return 0

    if matrix[y][x] != word[0]:
        return 0

    return _search_word(word[1:], matrix, x + direction[0], y + direction[1], direction)

def search_word(word, matrix):
    directions = [
        (-1, 0), (1, 0), # L/R
        (0, -1), (0, 1), # T/B
        (-1, -1), (1, -1), (-1, 1), (1, 1), # TL, TR, BL, BR
    ]

    count = 0

    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] != word[0]:
                continue
            for direction in directions:
                count += _search_word(word, matrix, col, row, direction)

    return count

def search_x_mas(matrix):
    count = 0

    for row in range(1, len(matrix) - 1):
        for col in range(1, len(matrix[row]) - 1):
            if matrix[row][col] != 'A':
                continue

            tl = matrix[row - 1][col - 1]
            tr = matrix[row + 1][col - 1]
            bl = matrix[row - 1][col + 1]
            br = matrix[row + 1][col + 1]

            if sorted([tl, tr, bl, br]) != ["M", "M", "S", "S"]:
                continue

            if tl == br or tr == bl:
                continue

            count += 1


    return count

def main():
    if len(sys.argv) < 2:
        print("missing required input file", file=sys.stderr)
        sys.exit(1)

    with open(sys.argv[1]) as f:
        lines = f.readlines()
        lines[-1] += "\n"

    print(f"#1: {search_word("XMAS", lines)}")
    print(f"#2: {search_x_mas(lines)}")

if __name__ == "__main__":
    main()