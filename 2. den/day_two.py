# *************************************
#               PART 1
# *************************************

depth = hor_pos = aim = 0

for data in open("input.txt","r"):
    key, value = data.split(" ")
    if key == "up": 
        depth += int(value)
    if key == "down": 
        depth -= int(value)
    if key == "forward": 
        hor_pos += int(value)
print("Part 1:",abs(depth*hor_pos))

# *************************************
#               PART 2
# *************************************

depth = hor_pos = aim = 0

for data in open("input.txt","r"):
    key, value = data.split(" ")
    if key == "up": 
        aim -= int(value)
    if key == "down": 
        aim += int(value)
    if key == "forward": 
        hor_pos += int(value)
        depth += aim * int(value)

print("Part 2:",abs(depth*hor_pos))










    

