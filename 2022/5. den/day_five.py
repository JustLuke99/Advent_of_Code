cargo_crane, cargo_crane_2, removed = [], [], []
space = False

def move(Xfrom, Xto):
    global removed, cargo_crane
    
    if not cargo_crane[Xfrom] == []:
        posledni = cargo_crane[Xfrom].pop()
        cargo_crane[Xto].append(posledni)
    
    if not cargo_crane_2[Xfrom] == []:
        removed.append(cargo_crane_2[Xfrom].pop())

def start(Xmove, Xfrom, Xto):
    global removed, cargo_crane
    removed = []
    while Xmove > 0:
        move(Xfrom, Xto)
        Xmove -= 1
        
    removed.reverse()
    for x in removed:
        cargo_crane_2[Xto].append(x)
        
for line in open("input.txt", "r"):
    if line.replace("\n", "") == "":
        space = True
        continue
    if not space:
        cargo_crane.append(line.replace("\n", "").split(" "))
        cargo_crane_2.append(line.replace("\n", "").split(" "))
    else:
        XXX = line.replace("\n", "").split(" ")
        start(int(XXX[0]), int(XXX[1])-1, int(XXX[2])-1)

print("Part 1:")
for x in cargo_crane:
    print(x)
    
print("Part 2:")
for x in cargo_crane_2:
    print(x)
    
