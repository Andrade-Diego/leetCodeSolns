def removeDuplicates(nums):
    if len(nums) <= 1: return len(nums)
    currPtr = 1
    prevPtr = 0
    while currPtr < len(nums):
        if nums[currPtr] == nums[prevPtr]:
            nums.pop(currPtr)
        else:
            prevPtr = currPtr
            currPtr += 1
    return len(nums)

if __name__ == "__main__":
    nums = [2, 7, 7, 11, 11, 11, 15, 15, 15, 15]
    print(f"(TEST)\n\tList: {nums}\n\tResult: {removeDuplicates(nums)}")