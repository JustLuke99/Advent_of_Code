files, test, current_dir = [], {}, ""

for line in open("input.txt", "r"):
    line = line.replace("\n", "").split(" ")
    if line[0] == "$":
        if line[1] == "cd":
            if line[2] == "..":
                current_dir = current_dir.rsplit("/",1)[0]
            else:
                current_dir += f"/{line[2]}"
    else:
        if not line[0] == "dir":
            files.append([current_dir, int(line[0])])
    
    test[current_dir] = 0

def add_to_dir(_dir, size):
    test[_dir] += size
    splited = _dir.rsplit("/", 1)[0]
    if splited != "/":
        add_to_dir(splited, size)

for file in files:
    add_to_dir(file[0], file[1])

part_1 = sum([x for x in test.values() if x < 100000])
part_2 = min(i for i in test.values() if i >= 30_000_000 - (70_000_000 - test["//"]))

print(f"Part 1: {part_1}")
print(f"Part 2: {part_2}") 
