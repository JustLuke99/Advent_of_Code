import numpy as np

data = open("input.txt", "r").read()
nums = np.array(data.split(","), int)

count_arr = np.bincount(nums)
count_arr = np.append(count_arr, [0]*5)
count_arr = np.roll(count_arr, 1)

for i in range(256):
    count_arr = np.roll(count_arr, -1)
    count_arr[7] += count_arr[0]
    count_arr[9] += count_arr[0]
    count_arr[0] = 0
    if i == 79:
        print(f"Part 1: {count_arr.sum()}")

print(f"Part 2: {count_arr.sum()}")


# *************************************
#               PART 1
# *************************************
#
# data = open("input.txt", "r").read()
# nums = np.array(data.split(","), int)
# 
# for _ in range(80):
#     nums -= 1
#     new = (nums < 0).sum()
#     nums[nums == -1] = 6
#     nums = np.append(nums, [8]*new)
#     
# print(f"Part 1: {len(nums)}")
