"""
Day 1
Advent of code 2022
"""

# ----------- Part 1 -----------

# read the input file
path = "input"
with open(file=path, mode="r") as file:
    content = file.readlines()

# create empty dictionary that will hold elves and their calorie packages
elfDict = {}

# each elf will have it's own list of calorie values
n = 0
for package in content:
    if package == "\n":
        n += 1
        continue
    # cast values to integers and append them to list of values with elf[n] as a key
    elfDict.setdefault(f"elf{n}", []).append(int(package))

# now to sum up calories for every elf
total = []
for key, value in elfDict.items():
    total.append(sum(value))

# format the output
print(
    f"""
Elf index: {total.index(max(total))}
Total calories: {max(total)}
Packages: {elfDict[f"elf{59}"]}
"""
)

# ----------- Part 2 -----------

# sort the total list and print the top 3
total.sort(reverse=True)
print("Total calories of top three elves")
print(total[0:3])
print(sum(total[0:3]))

# tags: exercise, dictionary, setdefault(), readline, i/o stream