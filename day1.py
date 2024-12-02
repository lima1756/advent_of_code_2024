file = open("./input/day1.txt", "r")


# Part 1
list1 = [] 
list2 = []
for line in file:
    ids = line.split("   ")
    list1.append(int(ids[0]))
    list2.append(int(ids[1]))

list1_s = sorted(list1)
list2_s = sorted(list2)

distance = 0

for i in range(len(list1_s)):
    distance += abs(list1_s[i] - list2_s[i])    

print(distance)

# Part 2

found_dict = {}

for id in list2:
    if id in found_dict:
        found_dict[id] += 1
    else:
        found_dict[id] = 1

total = 0
for id in list1:
    if id in found_dict:
        total += id * found_dict[id]

print(total)
    
