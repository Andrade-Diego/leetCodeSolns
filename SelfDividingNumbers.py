def selfDividingNumbers(left, right):
    def testNum(num):
        test = num
        while test != 0:

            # if smallest digit is 0, return false
            if test % 10 == 0:
                return False

            # if number is divisible by smallest digit, you can keep going
            elif num % (test % 10) == 0:
                test = test // 10

            # if number is not divisible by smallest digit, no use in continuing
            else:
                return False
        return True

    valid = []
    for i in range(left, right + 1):
        if testNum(i):
            valid.append(i)
    return valid


if __name__ == "__main__":
    left = 3
    right = 40
    print(f"(TEST)\n\tLeft Bound: {left}\n\tRight Bound: {right}\n\tResult: {selfDividingNumbers(left, right)}")
