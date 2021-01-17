def lengthOfLastWord(s):
    arr = [""]
    prev = None
    for char in s:
        if char != ' ' and prev == ' ':
            arr.append(char)
        elif char != ' ':
            arr[-1] += char
        prev = char
    return len(arr[-1])

if __name__ == "__main__":
    s = "This is the list of words we want to test"

    print(f"(TEST)\n\tString: {s}\n\tLength of Last Word: {lengthOfLastWord(s)}")
