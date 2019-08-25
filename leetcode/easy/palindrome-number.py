"""
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:

Input: 121
Output: true
Example 2:

Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

Follow up:

Could you solve it without converting the integer to a string?
"""


# time complexity O(n)
# This is a solution without converting integer to string, but not fast: 80ms
def isPalindrome_abandons(x: int) -> bool:
    num_origin, num_reversed= x, 0
    while x >= 1:
        digit = x % 10
        x //= 10
        num_reversed = num_reversed * 10 + digit
    print(num_origin, num_reversed)
    if num_origin == num_reversed:
        return True
    else:
        return False


# time complexity O(n)
# I used converting integer to string, but fast: 48ms
def isPalindrome(x: int) -> bool:
    str_x = str(x)
    if x >= 0 and str_x == str_x[::-1]:
        return True
    else:
        return False

inp = 121

print(isPalindrome(inp))
