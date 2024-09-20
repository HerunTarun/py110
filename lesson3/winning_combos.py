WINNING_COMBINATIONS = [
        [1, 2, 3], [4, 5, 6], [7, 8, 9],
        [1, 4, 7], [2, 5, 8], [3, 6, 9],
        [1, 5, 9], [3, 5, 7]
    ]


player_choices = {3, 4, 5}

list_choices = list(player_choices)

possible_combos = []

for combo in WINNING_COMBINATIONS:
    if not (set(combo) & player_choices):
        possible_combos.append(combo)

print(possible_combos)