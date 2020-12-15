def twoSum(nums, target):
    solns = {}
    for i, n in enumerate(nums):
        if n in solns:
            return [i, solns[n]]
        diff = target - n
        solns[diff] = i

if __name__ == "__main__":
    #testing the following list and target, should return [1, 3] or [3, 1]
    nums = [2, 7, 11, 15]
    target = 22
    print(f"(TEST)\n\tList: {nums}\n\tTarget: {target}\n\tResult: {twoSum(nums, target)}")