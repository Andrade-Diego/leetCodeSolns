from collections import Counter

def minSteps(s: str, t: str) -> int:
    sCounter = Counter(s)
    sCounter.subtract(t)
    changes = 0
    for char in sCounter.values():
        changes += char if char > 0 else 0
    return changes

if __name__ == "__main__":
    s = input('Enter a string: ')
    t = input('Enter another string of the same length: ')
    result = minSteps(s, t)
    print(f"\nThe number of changes needed to make the\nsecond string an anagram of the first is {result}")