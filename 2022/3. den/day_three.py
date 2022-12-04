# *************************************
#               PART 1
# *************************************

item_sum = 0
for line in open("input.txt", "r").read().split("\n"):
    first_bag, second_bag = line[0:len(line)//2], line[len(line)//2:]
    for char in list(set(first_bag)&set(second_bag)):
        item_sum += ord(char[0])-38 if char[0].isupper() else ord(char[0])-96
        
print(f"Part 1: {item_sum}")
   
# *************************************
#               PART 2
# *************************************   
    
file = open("input.txt", "r").read().split("\n")
item_sum, i = 0, 0
while i < 300:
    for char in list(set(file[i])&set(file[i+1])&set(file[i+2])):
        item_sum += ord(char[0])-38 if char[0].isupper() else ord(char[0])-96
    i += 3
    
print(f"Part 2: {item_sum}")
