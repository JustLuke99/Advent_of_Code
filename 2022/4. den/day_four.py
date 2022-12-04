count_1, count_2 = 0, 0
for line in open("input.txt", "r").read().split("\n"):
    first, second  = [list(map(int, x.split("-"))) for x in line.split(",")]
    first_list, second_list = list(range(first[0], first[1]+1)), list(range(second[0], second[1]+1))
    if not (list(set(first_list) - set(second_list))) or not (list(set(second_list) - set(first_list))):
        count_1 += 1   
    if set(first_list).intersection(set(second_list)):
        count_2 += 1      
        
print(f"Part 1: {count_1}")
print(f"Part 2: {count_2}")

