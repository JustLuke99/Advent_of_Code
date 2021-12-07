import numpy as np

nums = np.array((open("input.txt", "r").read()).split(","), int)

part_1, part_2 = [], []
for i in range(max(nums)):
    part_1.append(abs(np.array(nums, int) - i).sum())
    part_2.append(np.array([abs(num - i) * (abs(num - i) + 1) / 2 for num in nums], int).sum())

print(f"Part 1: {min(part_1)}")
print(f"Part 2: {min(part_2)}")

exit()

# *************************************
#          ONE LINE CHALLENGE
# *************************************

print((min(abs(np.array(np.array((open("input.txt", "r").read()).split(","), int), int) - i).sum() for i in range(max(np.array((open("input.txt", "r").read()).split(","), int))))), (min(np.array([int(abs(abs(num - i) * (abs(num - i) + 1) / 2)) for num in np.array((open("input.txt", "r").read()).split(","), int)]).sum() for i in range(max(np.array((open("input.txt", "r").read()).split(","), int))))))



