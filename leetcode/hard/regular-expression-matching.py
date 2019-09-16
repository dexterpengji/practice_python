"""
Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

Note:

s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like . or *.
Example 1:

Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input:
s = "aa"
p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
Example 3:

Input:
s = "ab"
p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".
Example 4:

Input:
s = "aab"
p = "c*a*b"
Output: true
Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore, it matches "aab".
Example 5:

Input:
s = "mississippi"
p = "mis*is*p*."
Output: false
"""


def isMatch(s: str, p: str) -> bool:
    state = 0       # 0: char mode; 1: * mode; 2: . mode
    char_curr_s, char_curr_p, char_any, char_repeat = None, None, None, None
    i_s, i_p, l_s, l_p = 0, 0, len(s), len(p)
    while True:
        char_curr_s = s[i_s]
        char_curr_p = p[i_p]
        if char_curr_p == "*":
            state = 1
            pass
        elif char_curr_p == ".":
            state = 2
            pass
        else:
            state = 0
            if char_curr_p != s[i_s]:
                return False
            else:
                i_s += 1
    return True


string = "mississippi"
pattern = "mis*is*p*."

print(isMatch(string, pattern))
