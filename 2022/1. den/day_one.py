import numpy as np
# *************************************
#               PART 1
# *************************************

max_val = 0
cal = 0

file = open("input.txt", "r")
for line in file.readlines():
        if line.strip():
            cal += int(line)
        else:
            if max_val < cal:
                max_val = cal
            cal = 0
            
print(f"Part 1: {max_val}") 

# *************************************

for line in open("input.txt", "r").readlines():
        cal += int(line) if line.strip() else (-cal)
        max_val = max_val if max_val > cal else cal
            
print(f"Part 1(M): {max_val}") 

# *************************************
#               PART 2
# *************************************

max_val = [0, 0, 0]
cal = 0

file = open("input.txt", "r")
for line in file.readlines():
        if line.strip():
            cal += int(line)
        else:
            for i in range(len(max_val)):
                if max_val[i] < cal:
                    max_val[i] = cal
                    break
                    
            cal = 0
            
print(f"Part 2: {sum(max_val)}") 

# *************************************

for line in open("input.txt", "r").readlines():
        cal += int(line) if line.strip() else (-cal)
        max_val = [val if cal < val else cal for val in max_val]

print(f"Part 2(M): {sum(max_val)}") 

# *************************************
#               TOGETHER
# *************************************

cal, max_val1, max_val1 = 0, 0, [0,0,0]

for line in open("input.txt", "r").readlines():
        cal += int(line) if line.strip() else (-cal)
        max_val1 = [val if cal < val else cal for val in max_val1]
        
print(f"Part 1(T): {max(max_val1)}\nPart 2(T): {sum(max_val1)}")

