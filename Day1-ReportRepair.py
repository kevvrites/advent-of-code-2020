# Find two entries that sum up to 2020 and return their product.

f = open("Day1-Input.txt")
lines = f.readlines()

#def reportRepair(lines, target):

hashmap = {}

for val in lines:
    ans = 2020 - int(val)
    hashmap[int(val)] = ans
for val in lines:
    ans = 2020 - int(val)
    if ans in hashmap:
        print(ans * int(val))