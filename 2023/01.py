# day 1, {2023}

import regex as re

# read data
with open('2023/data/01.txt', 'r') as file:
    data = file.read().split()

# review data formatting
print(data)

# part 1
def part_one(data):
    result = 0
    for text in data:
        numerical = "".join(re.findall("\d+", text))
        result += int(numerical[0] + numerical[-1])
    return result


print(f'Part one: {part_one(data)}')

# part 2
def part_two(data):
    MAP = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
        }
    
    REGEX = f"[1-9]|{'|'.join(key for key in MAP.keys())}"
    
    result = 0
    for text in data:
        matching = re.findall(REGEX, text, overlapped=True)
        first_number = matching[0] if matching[0].isdigit() else MAP[matching[0]]
        last_number = matching[-1] if matching[-1].isdigit() else MAP[matching[-1]]
        result += int(first_number + last_number)
    return result

print(f'Part two: {part_two(data)}')
