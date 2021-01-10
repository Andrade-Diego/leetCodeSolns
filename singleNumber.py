def singleNumber(nums):
    nums.sort()
    i = 0
    while i < len(nums):
        if i == len(nums) - 1:
            return nums[i]
        elif not nums[i] == nums[i + 1]:
            return nums[i]
        else:
            i += 2

nums = [2, 8, 3, 22, 3, 4, 4, 2, 22]
print(f"(TEST)\n\tList: {nums}\n\tResult: {singleNumber(nums)}")