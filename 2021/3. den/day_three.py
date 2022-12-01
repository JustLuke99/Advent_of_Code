# *************************************
#               PART 1
# *************************************

vysledek = [[0 for i in range(2)] for j in range(12)]
helper = 0

for line in open("input.txt", "r"):
    for num in line:
        if num == "\n":
            continue
        if int(num) == 0:
            vysledek[helper % 12][0] += 1
        else:
            vysledek[helper % 12][1] += 1
        helper += 1

gamma = ""
for col in vysledek:
    gamma += "0" if col[0] > col[1] else "1"

epsilon = gamma.replace('1', '2').replace('0', '1').replace('2', '0')

print(f"Part 1: {int(epsilon, 2)* int(gamma, 2)}")

# *************************************
#               PART 2
# *************************************

vysledek = []
zero = one = 0
for mode in range(2):
    first = "1" if mode == 0 else "0"
    second = "0" if mode == 0 else "1"
    
    with open("input.txt", "r") as file:
        data = [x for x in file.readlines()]

    for i in range(12):
        for line in data:
            if line[i] == "0":
                zero += 1
            else:
                one += 1
        
        if zero > one:
            data[:] = [x for x in data if not x[i] == first]
        
        elif zero < one or zero == one:
            data[:] = [x for x in data if not x[i] == second]

        zero = one =  0
        if len(data) == 1:
            break
    vysledek.append(data)

xo = co = ""
for x in vysledek[0]:
    xo += x
for c in vysledek[1]:
    co += c

print(f"Part 2: {int(xo,2)*int(co,2)}")

