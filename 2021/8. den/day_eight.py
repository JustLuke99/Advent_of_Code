# *************************************
#               PART 1
# *************************************

part_1 = 0
data = [(x.split(" | "))[1] for x in open("input.txt", "r")]

for line in data:
    part_1 += sum([1 if len(num) in [2, 4, 3, 7] else 0 for num in line.strip().split(" ")])

print(f"Part 1: {part_1}")
exit()
                 
# *************************************
#               PART 2
# ************************************* 

help = ["" for i in range(7)]
data = [(x) for x in open("input.txt", "r")]
data = data[0].split(" | ")
data[0] = data[0].split(" ")

print(data[0])
for num in data[0]:
    if len(num) == 2:
        help[2], help[5] = num, num
    if len(num) == 4:
        ...
    if len(num) == 7:
        ...
    if len(num) == 8:
        ...
print(help)

           