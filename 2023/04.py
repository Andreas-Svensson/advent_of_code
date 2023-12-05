# day 4, {2023}

# read data
with open('2023/data/04.txt', 'r') as file:
    data = file.read().splitlines()

# calculate amount of winning numbers per card
cards = {}
for i, line in enumerate(data):
    winning_numbers, scratched_numbers = [i.split() for i in line[line.find(":")+1:].split("|")]
    cards[i+1] = {}
    cards[i+1]["winning"] = len([i for i in winning_numbers if i in scratched_numbers])
    cards[i+1]["amount"] = 1 # default amount set to 1 to include self

# iterate through each card and increment amount of next cards based on amount
r1 = 0
for card_nr, card in cards.items():
    if card["winning"]:
        r1 += 2 ** (card["winning"] - 1)
        for _ in range(card["amount"]):
            for i in range(1, card["winning"]+1):
                cards[card_nr+i]["amount"] += 1

r2 = sum([card["amount"] for card in cards.values()])
print(r1, r2)
