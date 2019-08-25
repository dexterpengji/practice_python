"""
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21

Note: Assume we are dealing with an environment which could only store integers within the 32-bit signed integer
range: [−2 ** 31, 2 ** 31 − 1]. For the purpose of this problem, assume that your function returns 0 when the
reversed integer overflows.
"""

import math


# time complexity O(2n)
def reverse_abandoned(x: int) -> int:
    dev, digits, ret, i, sign = 1, [], 0, 0, 1
    if x < 0:
        sign = -1
        x *= -1
    while x >= 1:
        digits.append(x % 10)
        x //= 10
    while digits:
        ret += digits.pop(-1) * 10 ** i
        i += 1
    ret *= sign
    if -2 ** 31 <= ret <= 2 ** 31 - 1:
        return ret
    else:
        return 0


# time complexity O(n)
def reverse(x: int) -> int:
    ret, sign = 0, 1
    if x < 0:
        sign = -1
        x *= -1
    while x >= 1:
        ret = ret * 10 + x % 10
        x = x//10
    ret *= sign
    # if -2 ** 31 <= ret <= 2 ** 31 - 1:
    # range() indicates closed interval
    if ret in range(-2 ** 31, 2 ** 31 - 1):
        return ret
    else:
        return 0


x = -2147483412
# x = 123456789
print(reverse(x))
