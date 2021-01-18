def plusOne(digits):
    for i in range(len(digits) - 1, -1, -1):
        if digits[i] == 9:
            if i == 0:
                digits[i] = 0
                digits.insert(0, 1)
            else:
                digits[i] = 0
        else:
            digits[i] += 1
            break
    return digits

if __name__ == "__main__":
    digits = [9, 9, 9, 9]
    digits2 = [1, 2, 3, 9]
    print(f"(TEST1)\n\tDigits: {digits}\n\tDigits Plus One: {plusOne(digits)}")
    print(f"(TEST2)\n\tDigits: {digits2}\n\tDigits Plus One: {plusOne(digits2)}")
