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


def find_char(x, y):
    return [item for item in all_numbers if item['x'] == x and item['y'] == y]


def check(star_x, star_y):
    found_items = []
    for y in [star_y - 1, star_y + 1]:
        for x in range(star_x - 3, star_x + 2):
            item = find_char(x, y)
            if item:
                if not len(str(item[0]["number"])) < star_x - x:
                    found_items.append(item[0]["number"])

    for x in range(star_x - 3, star_x + 2):
        item = find_char(x, star_y)
        if item:
            if not len(str(item[0]["number"])) < star_x - x:
                found_items.append(item[0]["number"])

    return found_items


map = []
part_one, part_two = 0, 0

for line in open("input.txt", "r").readlines():
    map.append(line.strip())

# PART 1
for i, line in enumerate(map):
    numbers = re.finditer(r"\d+", line)
    stars = re.finditer(r"\*", line)

    numbers_positions = [(number.start(), int(number.group())) for number in numbers]
    stars_positions = [star.start() for star in stars]

    for position, value in numbers_positions:
        symbol = False

        for j in range(len(str(value))):
            if find_symbol(i, position + j):
                symbol = True

        if symbol:
            part_one += value

# PART 2
all_stars, all_numbers = [], []
for i, line in enumerate(map):
    for number in re.finditer(r"\d+", line):
        all_numbers.append({"x": number.start(), "y": i, "number": int(number.group())})

    for star in re.finditer(r"\*", line):
        all_stars.append({"x": star.start(), "y": i})

for star in all_stars:
    found_numbers = check(star["x"], star["y"])
    if len(found_numbers) == 2:
        part_two += found_numbers[0] * found_numbers[1]

print(f"Part 1: {part_one}")
print(f"Part 2: {part_two}")
