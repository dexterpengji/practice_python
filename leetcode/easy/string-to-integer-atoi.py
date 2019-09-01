"""
Implement atoi which converts a string to an integer.

The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned.

Note:

Only the space character ' ' is considered as whitespace character.
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. If the numerical value is out of the range of representable values, INT_MAX (231 − 1) or INT_MIN (−231) is returned.
Example 1:

Input: "42"
Output: 42
Example 2:

Input: "   -42"
Output: -42
Explanation: The first non-whitespace character is '-', which is the minus sign.
             Then take as many numerical digits as possible, which gets 42.
Example 3:

Input: "4193 with words"
Output: 4193
Explanation: Conversion stops at digit '3' as the next character is not a numerical digit.
Example 4:

Input: "words and 987"
Output: 0
Explanation: The first non-whitespace character is 'w', which is not a numerical
             digit or a +/- sign. Therefore no valid conversion could be performed.
Example 5:

Input: "-91283472332"
Output: -2147483648
Explanation: The number "-91283472332" is out of the range of a 32-bit signed integer.
Therefore INT_MIN (−231) is returned.
"""


def myAtoi(str: str) -> int:    # Overflow happens a lot
    # vars setting
    digits, digits_lock, sign, sign_lock = 0, 0, +1, 0

    # first part:
    str = str.strip()   # delete all blacks
    if len(str) == 0:   # return 0 if string is none
        return 0

    # second part:
    for x in str:
        try:
            digits, sign_lock = digits * 10 + int(x), 1

            # check if it overflows
            ret = digits * sign
            if ret >= 2 ** 31 - 1:
                return 2 ** 31 - 1
            elif ret <= - 2 ** 31:
                return - 2 ** 31

        except ValueError:
            if x == "+":
                if sign_lock == 0:
                    sign_lock = 1
                else:
                    return digits * sign
            elif x == "-":
                if sign_lock == 0:
                    sign, sign_lock = -1, 1
                else:
                    return digits * sign
            else:
                return digits * sign

    return digits * sign


def myAtoi(str: str) -> int:    # Overflow barely happens
    # vars setting
    digits, digits_lock, sign, sign_lock = 0, 0, +1, 0

    # first part:
    str = str.strip()   # delete all blacks
    if len(str) == 0:   # return 0 if string is none
        return 0

    # second part:
    for x in str:
        try:
            digits, sign_lock = digits * 10 + int(x), 1

        except ValueError:
            if x == "+":
                if sign_lock == 0:
                    sign_lock = 1
                else:
                    return min(max(digits * sign, - 2 ** 31), 2 ** 31 - 1)
            elif x == "-":
                if sign_lock == 0:
                    sign, sign_lock = -1, 1
                else:
                    return min(max(digits * sign, - 2 ** 31), 2 ** 31 - 1)
            else:
                return min(max(digits * sign, - 2 ** 31), 2 ** 31 - 1)

    return min(max(digits * sign, - 2 ** 31), 2 ** 31 - 1)


# inp = "42"
# inp = "     -42"
# inp = "4193 with words"
# inp = ""
# inp = "words and 987"
# inp = "91283472332"
# inp = "   -"
# inp = " "
inp = "        -+1"
print(myAtoi(inp))

