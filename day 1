
f = open("data.txt", "r")

elves = []
current_cals = 0
for line in f:
    if line == "\n":
        elves.append(current_cals)
        current_cals=0
    else:
        current_cals+=int(line.strip())

f.close()

print("Pt. 1:")
print(max(elves))

top_three = 0
for _ in range(3):
    current_max = max(elves)
    top_three += current_max
    elves.remove(current_max)

print()
print("Pt. 2")
print(top_three)
