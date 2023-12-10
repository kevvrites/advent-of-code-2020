# Find two entries that sum up to 2020 and return their product.

f = open("day1input.txt")
lines = f.readlines()

# Part 1 (Two Sum)
hashmap = {}

for val in lines:
    ans = 2020 - int(val)
    hashmap[int(val)] = ans
for val in lines:
    ans = 2020 - int(val)
    if ans in hashmap:
        print(ans * int(val))

# Part 2 (Three Sum)
nums = [int(_) for _ in lines]
nums = sorted(nums)

for i in range(len(nums)- 2):
    l = i + 1
    r = len(nums) - 1
    while l < r:
        if (nums[i] + nums[l] + nums[r] == 2020):
            print(nums[i]*nums[l]*nums[r])
            break
        elif (nums[i] + nums[l] + nums[r] < 2020):
            l += 1
        else:
            r -= 1