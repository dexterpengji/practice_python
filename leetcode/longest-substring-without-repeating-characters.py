"""
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""


def lengthOfLongestSubstring(s: str) -> int:
    dic = {}
    max_global = max_local = head_cur = 0
    for i, x in enumerate(s):
        if x in dic and dic[x] >= head_cur:
            max_global = max(max_global, max_local)
            max_local = i - dic[x]
            head_cur = dic[x] + 1
        else:
            max_local += 1
        dic[x] = i
    return max(max_global, max_local)


string = "abba"         # 2
print(lengthOfLongestSubstring(string))
string = "dvdf"         # 3
print(lengthOfLongestSubstring(string))
string = "bbbbbb"       # 1
print(lengthOfLongestSubstring(string))
string = "pwwkew"       # 3
print(lengthOfLongestSubstring(string))
string = "abcdef"       # 6
print(lengthOfLongestSubstring(string))
string = "abcabcbb"     # 3
print(lengthOfLongestSubstring(string))
