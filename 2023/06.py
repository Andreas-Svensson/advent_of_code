# day 6, {2023}

# read data
with open('2023/data/06.txt', 'r') as file:
    data = file.read().splitlines()

times = list(map(int, data[0].split()[1:]))
joined_time = int("".join(data[0].split()[1:]))

distances = list(map(int, data[1].split()[1:]))
joined_distance = int("".join(data[1].split()[1:]))


def get_winning_strategies(time, distance):
    winning_strategies = 0
    for i in range(1, time+1):
        if i * (time-i) > distance:
            winning_strategies += 1
    return winning_strategies


r1 = 1
for time, distance in zip(times, distances):
    r1 *= get_winning_strategies(time, distance)

r2 = get_winning_strategies(joined_time, joined_distance)
print(r1, r2)
