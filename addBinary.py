def addBinary(a, b):
    aPtr = len(a) - 1
    bPtr = len(b) - 1
    result = ""
    carryThe = 0
    while aPtr >= 0 or bPtr >= 0:
        aVal = int(a[aPtr]) if aPtr >= 0 else 0
        bVal = int(b[bPtr]) if bPtr >= 0 else 0
        s = aVal + bVal + carryThe
        if s == 0 or s == 1:
            result = str(s) + result
            carryThe = 0
        if s == 2 or s == 3:
            result = str(s - 2) + result
            carryThe = 1
        aPtr -= 1
        bPtr -= 1
    if carryThe == 1: result = "1" + result
    return result

a = "1110001101"
b = "1111011010"

print(f"(TEST)\n\ta: {a}\n\tb: {b}\n\tresult: {addBinary(a, b)}")
