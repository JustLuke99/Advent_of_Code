import numpy as np
# *************************************
#               PART 1
# *************************************

max = 0
cal = 0

file = open("input.txt", "r")
for line in file.readlines():
        if line.strip():
            cal += int(line)
        else:
            if max < cal:
                max = cal
            cal = 0
            
print(f"Part 1: {max}") 

# *************************************

for line in open("input.txt", "r").readlines():
        cal += int(line) if line.strip() else (-cal)
        max = max if max > cal else cal
            
print(f"Part 1(M): {max}") 

# *************************************
#               PART 2
# *************************************

max = [0, 0, 0]
cal = 0

file = open("input.txt", "r")
for line in file.readlines():
        if line.strip():
            cal += int(line)
        else:
            for i in range(len(max)):
                if max[i] < cal:
                    max[i] = cal
                    break
                    
            cal = 0
            
print(f"Part 2: {sum(max)}") 

# *************************************

for line in open("input.txt", "r").readlines():
        cal += int(line) if line.strip() else (-cal)
        max = [val if cal < val else cal for val in max]

print(f"Part 2(M): {sum(max)}") 

# *************************************
#               TOGETHER
# *************************************

cal, max1, max2 = 0, 0, [0,0,0]

for line in open("input.txt", "r").readlines():
        cal += int(line) if line.strip() else (-cal)
        max1 = max1 if max1 > cal else cal
        max2 = [val if cal < val else cal for val in max2]
        
print(f"Part 1(T): {max1}\nPart 2(T): {sum(max2)}")
