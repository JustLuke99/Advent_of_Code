import re

part_one, part_two = 0, {num: 1 for num in range(1, len(open("input.txt", "r").readlines()) + 1)}
for card in open("input.txt", "r").readlines():
    game_number = int(re.findall(r'\b\d+\b', card.split(":")[0])[0])
    winning_cards = re.findall(r'\b\d+\b', card.split(": ")[1].split(" | ")[0])
    my_cards = re.findall(r'\b\d+\b', card.split(": ")[1].split(" | ")[1])
    points_one, points_two = 0, 0

    for my_card in my_cards:
        if my_card in winning_cards:
            points_one = 1 if points_one == 0 else points_one * 2
            points_two += 1

    for _ in range(part_two[game_number]):
        for i in range(points_two):
            part_two[game_number + i + 1] += 1

    part_one += points_one

print(f"Part 1: {part_one}")
print(f"Part 2: {sum(part_two.values())}")
