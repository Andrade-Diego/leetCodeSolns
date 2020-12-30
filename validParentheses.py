def isValid(s):
    symbolStack = []
    pair = {"]": "[", 
            "}": "{",
            ")": "("}
    for i, char in enumerate(s):
        if char == "[" or char == "{" or char == "(":
            symbolStack.append(char)
        elif char == "]" or char == "}" or char == ")":
            if symbolStack == []:
                return False
            if pair[char] == symbolStack[-1]:
                symbolStack.pop()
            else: return False
    return symbolStack == []

if __name__ == "__main__":
    s = "(n!/(n-r)!]"
    print(f"(TEST)\n\tstring: {s}\n\tResult: {isValid(s)}")
    s = "[n!/(n-r)!]"
    print(f"(TEST 2)\n\tstring: {s}\n\tResult: {isValid(s)}")