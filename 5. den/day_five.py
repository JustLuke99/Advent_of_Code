import numpy as np

data = []
with open("input.txt", "r") as file:
    for line in file:
        tmp = [line.split(",") for line in line.strip().split(" -> ")]
        data.append({"x1":int(tmp[0][0]),"y1":int(tmp[0][1]),"x2":int(tmp[1][0]),"y2":int(tmp[1][1])})

here = np.zeros((1000,1000), int)
part_2 = []
for one in data:
    if one["y1"] == one["y2"]:
        for i in range(min(one["x1"], one["x2"]), max(one["x1"], one["x2"])+1):       
            here[one["y1"]][i] += 1
    elif one["x1"] == one["x2"]:
        for i in range(min(one["y1"], one["y2"]), max(one["y1"], one["y2"])+1):
            here[i][one["x1"]] += 1
    else:
        part_2.append(one)

print(f"Part 1: {(here > 1).sum()}")

for one in part_2:
    dx = 1 if one["x2"] > one["x1"] else -1
    dy = 1 if one["y2"] > one["y1"] else -1
    for i in range(abs(one["x2"] - one["x1"])+1):
            here[one["y1"]+(i*dy)][one["x1"]+(i*dx)] += 1
    
print(f"Part 2: {(here > 1).sum()}") 