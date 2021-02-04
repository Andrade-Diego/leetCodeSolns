def isPalindrome(s):
    slist = [char.lower() for char in s if char.isalnum()]
    return slist == slist[::-1]


s = "A man, a plan, a canal: Panama"
print(f"(TEST)\n\tstring: {s}\n\tResult: {isPalindrome(s)}")
