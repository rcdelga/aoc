import os
import math

file_name = "input.txt"
base_directory = os.path.dirname(__file__)
input_file_path = os.path.join(base_directory, file_name)

file_input = None
with open(input_file_path, 'r') as file:
    file_input = file.read()

LIMITS = {'red': 12, 'green': 12, 'blue': 14}

winning_game_ids = []
winning_game_power_sets = []
for line in file_input.strip().split("\n"):
    game_num, data = line.split(":")
    game_id = game_num.split(" ")[1]

    grab_results = []
    game_totals = {'red': 0, 'green': 0, 'blue': 0}
    for hand_grab in data.split(";"):
        color_results = []
        for color_amount in hand_grab.split(","):
            amount, color = color_amount.strip().split(" ")
            if int(amount) > game_totals[color]:
                game_totals[color] = int(amount)
            color_results.append(int(amount) <= LIMITS[color])
        grab_results.append(all(color_results))
    winning_game = all(grab_results)
    if winning_game:
        winning_game_ids.append(int(game_id))
    winning_game_power_sets.append(math.prod(game_totals.values()))

print(sum(winning_game_ids)) # 2449
print(sum(winning_game_power_sets)) # 63981
