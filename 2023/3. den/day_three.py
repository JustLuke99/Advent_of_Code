import re


def find_symbol(start_x, start_y) -> bool:
    for x in range(start_x - 1, start_x + 2):
        if x < 0 or x >= 140:
            continue
        for y in range(start_y - 1, start_y + 2):
            if y < 0 or y >= 140:
                continue
            if not map[x][y].isdigit() and map[x][y] != ".":
                return True

    return False


map = []
part_one = 0

for line in open("input.txt", "r").readlines():
    map.append(line.strip())

for i, line in enumerate(map):
    numbers = re.finditer(r"\d+", line)
    stars = re.finditer(r"\*", line)

    positions_and_values = [(number.start(), int(number.group())) for number in numbers]
    positions_and_values2 = [(number.start(), number.group()) for number in stars]

    for position, value in positions_and_values:
        symbol = False
        for j in range(len(str(value))):
            if find_symbol(i, position + j):
                symbol = True

        if symbol:
            part_one += value

print(part_one)
