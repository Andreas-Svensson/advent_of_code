# day 5, {2023}

# read data
with open('2023/data/05.txt', 'r') as file:
    data = file.read().replace("map:", "").replace(":", "")


# part 1
def part_one(data):
    data_list = data[data.find("\n"):].split()
    data_dict = {}
    temp = []
    for i in data_list:
        if not i.isnumeric():
            last_key = i
            data_dict[i] = []
        else:
            temp.append(int(i))
            if len(temp) == 3:
                data_dict[last_key].append(temp)
                temp = []
    seeds = data[6:data.find("\n")].split()
    seeds = list(map(int, seeds))
    result = 10000000000
    for seed in seeds:
        temp = seed
        for values in data_dict.values():
            for destination, source, range in values:
                if source <= temp <= source + range-1:
                    diff = temp-source
                    temp = destination+diff
                    break
        result = min(result, temp)
    return result

print(f'Part one: {part_one(data)}')


# part 2
def part_two(data):
    # NOTE: extremely ugly brute-force solution (takes about 2 min)
    # work backwards starting at 0 until valid seed number is found
    # improve: only iterate over numbers in range of last map in order from smallest to largest
    data = data.replace("map:", "").split("\n\n")
    seeds = []
    seeds, *rest = [i.split()[1:] for i in data]
    rest = [[list(map(int, sublist[i:i+3])) for i in range(0, len(sublist), 3)] for sublist in rest]
    found = False
    i = 0
    rest[-1] = sorted(rest[-1], key=lambda x: x[1])
    while not found:
        temp = i
        for step in rest[::-1]:
            for instance in step:
                destination, source, range_val = instance
                if destination <= temp <= destination+range_val-1:
                    temp = temp+(source-destination)
                    break
        seeds = list(map(int, seeds))
        for x in zip(seeds[::2], seeds[1::2]):
            source, range_val = x
            if source <= temp <= source+range_val-1:
                return i
        i+=1

print(f'Part two: {part_two(data)}')
