data = [x.strip() for x in open("input.txt", "r").readlines()]
global huh
huh = 0

def porovnani(x1,y1,x2,y2) -> bool:
    try:
        if int(data[x1][y1]) > int(data[x2][y2]):
            global huh
            huh += 1
            porovnani(x,y-1,x,y)
            porovnani(x,y+1,x,y)
            porovnani(x-1,y,x,y)
            porovnani(x+1,y,x,y)
            return True
    except:
        return True
    return False


part_2 = []
vysl = 0
for x in range(5):
    for y in range(10):
        huh = 0
        if porovnani(x,y-1,x,y) and porovnani(x,y+1,x,y) and porovnani(x-1,y,x,y) and porovnani(x+1,y,x,y):
            vysl += int(data[x][y]) + 1
            part_2.append(huh)
                      
##print(vysl)
        