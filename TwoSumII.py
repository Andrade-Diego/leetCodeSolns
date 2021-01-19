def twoSum(numbers, target):
    check = {}
    curr = 0
    while curr < len(numbers):
        if numbers[curr] in check:
            return [check[numbers[curr]] + 1, curr + 1]
        else:
            check[target - numbers[curr]] = curr
        curr += 1

if __name__ == "__main__":
    #testing the following list and target, should return [1, 3] or [3, 1]
    nums = [2, 7, 11, 15]
    target = 18
    print(f"(TEST)\n\tList: {nums}\n\tTarget: {target}\n\tResult: {twoSum(nums, target)}")
