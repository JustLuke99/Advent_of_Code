string = open("input.txt", "r").read()
counter = 0
for i in range(len(string)):
    duplicate_chars = []
    for character in string[i:i+14]:       
        if character not in duplicate_chars:
            duplicate_chars.append(character)
    if len(duplicate_chars) != 14:
        counter += 1
    else:
        break

print(counter+14) 


