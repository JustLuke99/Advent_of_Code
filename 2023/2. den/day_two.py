MAX = {
   "red": 12,
   "green": 13,
   "blue": 14
}
part_one, part_two = 0, 0

for line in open("input.txt", "r").readlines():
    line = line.strip()
    game_id = line.split(":")[0].split(" ")[1]
    games = line.split(": ")[1].split("; ")
    possible = True
    game_max = {
       "red": 0,
       "green": 0,
       "blue": 0
    }

    for game in games:
        for round in game.split(", "):
            number, color = round.split(" ")

            if MAX[color] < int(number):
                possible = False

            if game_max[color] < int(number):
                game_max[color] = int(number)

    if possible:
        part_one += int(game_id)

    part_two += game_max["blue"] * game_max["red"] * game_max["green"]

print(f"Part 1: {part_one}")
print(f"Part 2: {part_two}")