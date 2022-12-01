# *************************************
#               PART 1
# *************************************

result = 0
last_num = 9999

for num in open("input.txt","r"):
    if int(num) > last_num:
        result += 1
    last_num = int(num)

print(f"Part 1: {result}")

# *************************************
#               PART 2
# *************************************

last_num = 9999
result = helper = num_1 = num_2 = num_3 = vysledek = 0

for num in open("input2.txt","r"):
    if helper % 3 == 0:
        num_1 = int(num)
    elif helper % 3 == 1:
        num_2 = int(num)
    elif helper % 3 == 2:
        num_3 = int(num)
    if helper >= 2:
        vysledek = num_1 + num_2 + num_3
        if vysledek > last_num: 
            result += 1
        last_num = vysledek
    helper += 1

print(f"Part 2: {result}") 