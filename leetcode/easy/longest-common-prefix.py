"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.
"""


def longestCommonPrefix(strs):
    ret, num = "", 0
    l = len(strs)
    # when there is only 1 string in the list
    if l == 1:
        return strs[0]
    # when nothing in the list
    elif l == 0:
        return ""
    # when it is normal, there are several strings in the list
    else:
        # find the shortest string in the list
        min_size, min_num = len(strs[0]), 0
        for j, z in enumerate(strs):
            min_size_checking = len(z)
            if min_size_checking < min_size:
                min_size, min_num = min_size_checking, j
            else:
                pass

        # find the first different alphabet, then return the longest prefix.
        for i, x in enumerate(strs[min_num]):
            for y in strs:
                if x == y[i]:
                    num += 1
                else:
                    return ret
            if num == l:
                ret += x
                num = 0
            else:
                return ret
        return ret


inp = [""]
out = longestCommonPrefix(inp)
print(out, type(out))
