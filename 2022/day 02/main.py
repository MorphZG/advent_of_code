"""
Day 2
Advent of code 2022
"""

# ----------- Part 1 -----------

hand_score = {"X": 1, "Y": 2, "Z": 3}
victories = [["C", "X"], ["A", "Y"], ["B", "Z"]]  # winning hands
draws = [["A", "X"], ["B", "Y"], ["C", "Z"]]  # draw hands


with open("input", mode="r") as file:
    content = file.readlines()

actions = []
for line in content:
    game_round = line.split()
    actions.append(game_round)

# count score
score = 0
for action in actions:
    if action in victories:
        score += 6
    elif action in draws:
        score += 3
    for hand in action[1]:
        score += hand_score[hand]

print(f"part 1 score count: {score}")

# ----------- Part 2 -----------

# win = 'Z'; draw = 'Y'; loss = 'X';
outcome_score = {"X": 0, "Y": 3, "Z": 6}
# rock = 'A'; paper = 'B'; scissors = 'C';
hand_score = {"A": 1, "B": 2, "C": 3}
A_play = {"win": "B", "draw": "A", "loss": "C"}
B_play = {"win": "C", "draw": "B", "loss": "A"}
C_play = {"win": "A", "draw": "C", "loss": "B"}

score = 0
for action in actions:

    if action[1] == "X":
        score += outcome_score["X"]
        if action[0] == "A":
            score += hand_score[A_play["loss"]]
        elif action[0] == "B":
            score += hand_score[B_play["loss"]]
        elif action[0] == "C":
            score += hand_score[C_play["loss"]]
    elif action[1] == "Y":
        score += outcome_score["Y"]
        if action[0] == "A":
            score += hand_score[A_play["draw"]]
        elif action[0] == "B":
            score += hand_score[B_play["draw"]]
        elif action[0] == "C":
            score += hand_score[C_play["draw"]]
    elif action[1] == "Z":
        score += outcome_score["Z"]
        if action[0] == "A":
            score += hand_score[A_play["win"]]
        elif action[0] == "B":
            score += hand_score[B_play["win"]]
        elif action[0] == "C":
            score += hand_score[C_play["win"]]


print(f"part 2 score count: {score}")


# tags: exercise,