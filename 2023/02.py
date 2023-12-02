# day 2, {2023}

# read data
with open('2023/data/02.txt', 'r') as file:
    data = file.read().splitlines()

# review data formatting
print(data)


def get_max_color(line):
    """get max amt of each color represented in a single game"""
    max_color = {
        "red": 0,
        "blue": 0,
        "green": 0
    }
    line = line[line.find(":")+2:] # remove "Game #: "
    for turn in line.split("; "): # -> ["1 red, 2 blue, 3 green", ...]
        for color in turn.split(", "): # -> [["1 red", "2 blue", "3 green"], ...]
            color = color.split() # -> [["1", "red"], ["2", "blue"], ["3", "green"]]
            max_color[color[1]] = max(int(color[0]), max_color[color[1]])
    return max_color


# part 1
def part_one(data):
    result = 0
    for line in data:
        game_id = int(line[5:line.find(":")])
        max_color = get_max_color(line)
        if max_color["red"] <= 12 and max_color["green"] <= 13 and max_color["blue"] <= 14:
            result += game_id
    return result

print(f'Part one: {part_one(data)}')


# part 2
def part_two(data):
    result = 0
    for line in data:
        max_color = get_max_color(line)
        result += max_color["red"] * max_color["green"] * max_color["blue"]
    return result

print(f'Part two: {part_two(data)}')
