data = [x.strip() for x in open("input.txt", "r").readlines()]
out = {")": 0, "]": 0, "}": 0, ">": 0}
brac = {")":"(", "]":"[", "}":"{", ">":"<"}
help2 = {"(": 1, "[": 2, "{": 3, "<": 4}
part_2 = []

for line in data:
    open = []
    Fbreak = False
    for br in line:
        if br in "([{<":
            open.append(br)
        else:
            if open[-1] is not brac[br]:
                out[br] += 1
                Fbreak = True
                break
            open = open[:-1]
    if Fbreak:
        continue
    val = 0
    for br in reversed(open):
        val *= 5
        val += help2[br]
    part_2.append(val)     
    
print(f"Part 1: {out[')'] * 3 +out[']'] * 57 + out['}'] * 1197 +out['>'] * 25137}")
print(f"Part 2: {sorted(part_2)[int(len(part_2)/2)]}") 
