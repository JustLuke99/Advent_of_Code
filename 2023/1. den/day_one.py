nums = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9, "zero": 0}
part_one, part_two = 0, 0

for line in open("input.txt", "r").readlines():
    numbers = []

    for i, char in enumerate(line):
        if char.isdigit():
            numbers.append({"number": char, "position": i})

    part_one += int(f"{numbers[0]['number']}{numbers[-1]['number']}")

    for number in nums.keys():
        pos = line.find(number)
        while pos != -1:
            numbers.append({"number": nums[number], "position": pos})
            pos = line.find(number, pos + 1)

    numbers.sort(key=lambda x: x['position'])
    part_two += int(f"{numbers[0]['number']}{numbers[-1]['number']}")

print(f"Part 1: {part_one}")
print(f"Part 2: {part_two}")
