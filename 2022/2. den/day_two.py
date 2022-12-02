# *************************************
#               PART 1
# *************************************

score = 0
for line in open("input.txt","r"):
    enemy, me = line.replace("\n", "").split(" ")
    
    if me == "X":
        score += 1
    elif me == "Y":
        score += 2
    elif me == "Z":
        score += 3
    
    if(me == "X" and enemy == "A") or (me == "Y" and enemy == "B") or (me == "Z" and enemy == "C"):
        score += 3
    elif (me == "X" and enemy == "C") or (me == "Y" and enemy == "A") or (me == "Z" and enemy == "B"):
        score += 6

print(f"Part 1: {score}") 

# *************************************
#               PART 2
# *************************************

score = 0
for line in open("input.txt","r"):
    enemy, winner = line.replace("\n", "").split(" ")
    
    if winner == "Y":
        score += 3
    elif winner == "Z":
        score += 6
    
    if(winner == "Y" and enemy == "C") or (winner == "Z" and enemy == "B") or (winner == "X" and enemy == "A"):
        score += 3
    elif (winner == "Y" and enemy == "B") or (winner == "Z" and enemy == "A") or (winner == "X" and enemy == "C"):
        score += 2
    elif (winner == "Y" and enemy == "A") or (winner == "Z" and enemy == "C") or (winner == "X" and enemy == "B"):
        score += 1

print(f"Part 2: {score}")
