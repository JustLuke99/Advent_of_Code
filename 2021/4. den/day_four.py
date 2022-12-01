import numpy as np

data = open("input.txt", "r").read().split("\n\n")
 
called_nums = np.fromstring(data[0], dtype=int, sep=",")    

plr_arr = []
first = last = wins = hp = 0

for arr in data:
    if not hp:
        hp += 1
        continue
    a = np.fromstring(arr, dtype=int, sep=" ")
    b = np.reshape(a, (5, 5))
    plr_arr.append({"win": False, "board": b}) 
    hp += 1
    
for num in called_nums:
    for arr in plr_arr:  
        arr["board"][arr["board"] == num] = -1
        if not arr["win"]:
            if True in np.all(arr["board"] == -1,axis= 0) or True in np.all(arr["board"] == -1,axis= 1):
                if not first:
                    arr["board"][arr["board"] == -1] = 0
                    first = num*arr["board"].sum()
                elif len(plr_arr)-1 == wins:
                    arr["board"][arr["board"] == -1] = 0
                    last = num*arr["board"].sum()
                    print(f"First: {first}")
                    print(f"Last: {last}") #11507, 9216 moc vysoko
                    exit()
                arr["win"] = True
                wins += 1