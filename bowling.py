def score(game):
    result = 0
    frame = 1
    is_first_try = True
    game = game.lower()

    for roll_num in range(len(game)):
        result += get_value(game[roll_num]) + calculate_bonus(game, roll_num, frame)

        # next roll is new frame?
        if not is_first_try:
            frame += 1
        is_first_try = not is_first_try
        if is_strike(game, roll_num):
            is_first_try = True
            frame += 1

    return result


def calculate_bonus(game, roll_num, frame):
    bonus = 0
    if is_spare(game, roll_num):
        bonus -= get_value(game[roll_num - 1])
    if is_in_game(frame) and (is_strike(game, roll_num) or is_spare(game, roll_num)):
        bonus += get_value(game[roll_num + 1])
        if is_strike(game, roll_num):
            bonus += get_value(game[roll_num + 2])
            if is_spare(game, roll_num + 2):
                bonus -= get_value(game[roll_num + 1])
    return bonus


def is_strike(game, roll_num):
    return game[roll_num] == 'x'


def is_spare(game, roll_num):
    return game[roll_num] == '/'


def is_in_game(frame):
    return frame < 10


def get_value(char):
    SCORE_TABLE = {
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "x": 10,
        "/": 10,
        "-": 0,
    }

    try:
        return SCORE_TABLE[char]
    except ValueError:
        raise ValueError()
