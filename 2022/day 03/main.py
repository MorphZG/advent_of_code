"""
Day 3
Advent of code 2022
"""

# -- part 1
# input == list of all items
# every item type is identified by single lower or uppercase letter (a is one item and A is another)
# each line of text represents a list of items in a single rucksack
# split the line in half and you will get items in left and right compartment
# find common items in left and right
# each item have value, give the sum of common items
# itmes from a to z have value 1 to 26
# items from A to Z have value 27 to 52

from collections import Counter
from string import ascii_letters as letters


solution: int = 0  # 7997

def get_score(char: str) -> int:
    # construct the counter
    # a: 1, z: 26, A:27, Z: 52
    counter = Counter(letters)
    value = 0
    for key in counter.keys():
        counter[key] += value
        value += 1
    return counter[char]


# read the input file
with open("input") as file:
    # read() as single large string, splitlines() on every white space
    content = file.read().splitlines()
# split the each string to left and right half
for line in content:
    n = len(line)
    if n % 2 == 1:
        print("Item is not even after split")
    else:
        print("\n----- Next item -----")
        leftCompartment = line[0 : n // 2]
        rightCompartment = line[n // 2 :]
        print(f"left: {leftCompartment}\nright: {rightCompartment}")
        # list the common letter in left and right compartment
        for letter in leftCompartment:
            if letter in rightCompartment:
                solution += get_score(letter)
                print(f"match: {letter}, score: +{get_score(letter)}")
                # when match is found go to next item, prevent duplicates
                break

print(f"\nPart 1, solution: {solution}")

# ---------- Part 2 ----------
# each group consists of three lines, each line is a group member
# each line holds the group id (badge), item type common for all three lines in a group
# find the group id of all groups
# count the score using the values from part 1

solution: int = 0  # 2545

# construct the groups of three lines
groups = []
for i in range(0, len(content), 3):
    # i is every third index
    # slice from content[i] to content[i+3]
    groups.append(content[i : i + 3])

for group in groups:
    line1 = group[0]
    line2 = group[1]
    line3 = group[2]
    for char in line1:
        if char in line2 and char in line3:
            solution += get_score(char)
            break

print(f"\nPart 2, solution: {solution}\n")

#modules: collections
#tags: exercise