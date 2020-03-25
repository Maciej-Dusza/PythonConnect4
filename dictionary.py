# BOARD SIZE
board_height = 5
board_width = 6

board_height_range = range(0, board_height+1)
board_width_range = range(0, board_width+1)

# MOVES FOR CHECK (verticall, horizontall, slant left up, slant left down)
directions = [[-1, 0], [0, 1], [-1, 1], [1, 1]]


# ALGORITM WEIGHTS
attack_ratio = 2
defense_ratio = 1

# Bonus for players color in checked 4
bonus = [10, 30, 1000]
