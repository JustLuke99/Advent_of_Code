array, visible, max = [], 0, 0

def tree_test(list, num):
    counter = 0
    for i in list:
        if int(i) < int(num):
            counter += 1
        elif int(i) >= int(num):
            counter += 1
            return counter
    return counter

def visible_test(row_num, col_num, num):
    global array, max
    
    left, right = [i for i in array[row_num][:col_num]], [i for i in array[row_num][col_num+1:]]
    up, down = [array[i][col_num] for i in range(0, row_num)], [array[i][col_num] for i in range(row_num+1, len(array))]
    
    up_value, down_value = tree_test(up[::-1], num), tree_test(down, num)
    left_value, right_value = tree_test(left[::-1], num), tree_test(right, num)
    
    val = up_value * down_value * left_value * right_value
    if val > max:
        max = val
    
    if row_num == 0 or col_num == 0 or row_num == len(array)-1 or col_num == len(array[0])-1:
        return True
    if sum(i >= num for i in left) == 0 or sum(i >= num for i in right) == 0:
        return True
    if sum(i >= num for i in up) == 0 or sum(i >= num for i in down) == 0:
        return True
    return False

for line in open("input.txt", "r").read().split("\n"):
    array.append(line)

for row_num, line in enumerate(array):
    for col_num, num in enumerate(line):
        if visible_test(row_num, col_num, num):
            visible += 1
 
print(f"Part 1: {visible}")
print(f"Part 2: {max}") 
