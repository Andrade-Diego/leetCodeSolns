def removeElement(nums, val):
    while nums.count(val):
        nums.remove(val)
    return len(nums)

nums = [2, 8, 3, 22, 3, 4, 4, 2, 22]
val = 4
print(f"(TEST)\n\tList: {nums}\n\tValue to remove: {val}\n\tResult Length: {removeElement(nums, val)}\n\tResult List : {nums}")