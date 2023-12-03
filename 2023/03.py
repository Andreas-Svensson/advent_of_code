# day 3, {2023}

import regex as re
from itertools import product
from math import prod

# read data
with open('2023/data/03.txt', 'r') as file:
    data = file.read()

# review data formatting
print(data)


def search_adjacent(data, x, y, searched_indices=[]):
    found_numbers = []
    for x_pos, y_pos in product([x-1, x, x+1], [y-1, y, y+1]): # iterate over 3x3 grid centered on x, y

        # avoid negative and out-of-range indices
        if y_pos < 0 or y_pos < 0:
            break
        if y_pos >= len(data) or x_pos >= len(data[y_pos]):
            break

        # if unsearched position
        if data[y_pos][x_pos].isdigit() and (x_pos, y_pos) not in searched_indices:
            searched_indices.append((x_pos, y_pos))

            # get lowest index of number
            min_index = x_pos
            while min_index - 1 >= 0 and data[y_pos][min_index - 1].isdigit():
                min_index -= 1
                searched_indices.append((min_index, y_pos))

            # get highest index of number
            max_index = x_pos
            while max_index + 1 < len(data[y_pos]) and data[y_pos][max_index + 1].isdigit():
                max_index += 1
                searched_indices.append((max_index, y_pos))

            found_numbers.append(int(data[y_pos][min_index:max_index+1]))
    return found_numbers


# part 1
def part_one(data):
    searched_indices = []
    result = 0
    symbols = set(re.sub("[0-9.\n]", "", data))
    data = data.splitlines()
    for y, row in enumerate(data):
        for x, char in enumerate(row):
            if char in symbols:
                found_numbers = search_adjacent(data, x, y, searched_indices)
                result += sum(found_numbers)
    return result

print(f'Part one: {part_one(data)}')


# part 2
def part_two(data):
    result = 0
    symbol = "*"
    data = data.splitlines()
    for y, row in enumerate(data):
        for x, char in enumerate(row):
            if char == symbol:
                found_numbers = search_adjacent(data, x, y)
                result += prod(found_numbers) if len(found_numbers) >= 2 else 0
    return result

print(f'Part two: {part_two(data)}')
