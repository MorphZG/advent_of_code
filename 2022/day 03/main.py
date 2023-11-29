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
# -- part 2
# input is split in groups, each with 3 lines
# find item common in every line of the group
# not sure about this: "...at most two of the Elves will be carrying any other item type."


from collections import Counter
from string import ascii_letters as letters
from itertools import zip_longest

# ---------- Part 1 ---------- 

solution: int = 0  # 7997

# set the counter
# a: 1, z: 26, A:27, Z: 52
counter = Counter(letters)
value = 0
for char, base in counter.items():
    counter[char] += value
    value += 1


# read the input file
with open("input") as file:
    content = file.readlines()
# split the each string to left and right half
all_items = []
matching_letters = []
for line in content:
    line = line.rsplit("\n")[0]  # removes the \n from string
    n = len(line)
    if n % 2 == 1:
        print("Item is not even after split")
    else:
        print("\n----- Next item -----")
        leftCompartment = line[0 : n // 2]
        rightCompartment = line[n // 2 :]
        left_right = []
        left_right.append(leftCompartment)
        left_right.append(rightCompartment)
        all_items.append(left_right)
        print(f"left: {leftCompartment}\nright: {rightCompartment}")
        # list the common letters in left and right compartment
        for letter in leftCompartment:
            if letter in rightCompartment:
                matching_letters.append(letter)
                solution += counter[letter]
                print(f"match: {letter}, score: +{counter[letter]}")
                break # prevents duplicates, when match is find go to next item

print(f"\ntotal score: {solution}\n")

# ---------- Part 2 ---------- 

solution: int = 0  # 0000

def grouper(iterable, n, *, incomplete='strict', fillvalue=None):
    "Collect data into non-overlapping fixed-length chunks or blocks"
    # grouper('ABCDEFG', 3, fillvalue='x') --> ABC DEF Gxx
    # grouper('ABCDEFG', 3, incomplete='strict') --> ABC DEF ValueError
    # grouper('ABCDEFG', 3, incomplete='ignore') --> ABC DEF
    args = [iter(iterable)] * n
    if incomplete == 'fill':
        return zip_longest(*args, fillvalue=fillvalue)
    if incomplete == 'strict':
        return zip(*args, strict=True)
    if incomplete == 'ignore':
        return zip(*args)
    else:
        raise ValueError('Expected fill, strict, or ignore')


# separate full and clean lines
full_lines = []
for line in content:
    full_lines.append(line.rsplit("\n")[0])  # remove \n and apend to list

# build groups of 3 lines
test = grouper(full_lines, n=3)
for group in test:
    print(group)




#modules: collections
#tags: exercise
