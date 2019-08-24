"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
"""


# time complexity: O(n)
def isPalindrome_abandoned(s: str) -> str:
    l = len(s)
    if l % 2 == 1:
        origin = s[:l // 2]
        mirror = s[l // 2 + 1:]
    else:
        origin = s[:l // 2]
        mirror = s[l // 2:]
    for i, x in enumerate(origin):
        if x != mirror[-(1 + i)]:
            return False
    return True


# time complexity: O(1)
def isPalindrome(s: str) -> str:
    if s == s[::-1]:
        return True
    else:
        return False


# time complexity: O(n**2)
def longestPalindrome_abandoned(s: str) -> str:
    l = len(s)
    max_global = max_local = [0, ""]
    for i, x in enumerate(s):
        for j, y in enumerate(s[i:]):
            checking = s[i:i + j + 1]
            if checking == checking[::-1]:
                max_local = [len(checking), checking]
        if max_global[0] < max_local[0]:
            max_global = max_local
    return max_global[1]


# time complexity: O(n)
def longestPalindrome(s: str) -> str:
    # Return if string is empty
    if not s:
        return s

    res = ""
    for i in range(len(s)):
        j = i + 1
        # While j is less than length of string
        # AND res is *not* longer than substring s[i:]
        while j <= len(s) and len(res) <= len(s[i:]):
            # If substring s[i:j] is a palindrome
            # AND substring is longer than res
            if s[i:j] == s[i:j][::-1] and len(s[i:j]) > len(res):
                res = s[i:j]
            j += 1

    return res


inp = "babad"
# print(longestPalindrome_forcingCal(inp))
print(longestPalindrome(inp))

inp = "cbbd"
# print(longestPalindrome_forcingCal(inp))
print(longestPalindrome(inp))

inp = "abababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababa"
# print(longestPalindrome_forcingCal(inp))
print(longestPalindrome(inp))
