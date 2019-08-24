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
    len_s = len(s)
    ret_tempt, ret = 1, len_s
    for i in range(len_s):
        char_step = s[i]
        for j in range(i + 1, len_s):
            char_check = s[j]
            len_now = j - i + 1
            if char_check == char_step:
                print("%s ===" % char_check)
                if len_now > ret_tempt:
                    ret_tempt = len_now
                break
            else:
                pass
        if ret_tempt < ret:
            ret = ret_tempt
    return ret


string = "abcdef"
print(lengthOfLongestSubstring(string))
