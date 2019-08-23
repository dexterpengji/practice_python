"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""

List = [2, 7, 11, 15]
Target = 9

List = [3, 2, 4]
Target = 6

List = [3, 3]
Target = 6


class Solution:
    def __init__(self, nums, target):
        self.nums = nums
        self.target = target

    # time complexity: O(n)
    def twoSum(self) -> List:
        dic = {}
        for x in range(len(self.nums)):
            dic[self.nums[x]] = x
        for x in range(len(self.nums)):
            # print(self.target, self.nums[x])
            dif = self.target - self.nums[x]
            if dif in dic and x != dic[dif]:
                return x, dic[dif]

    # time complexity: O(n)
    def twoSum_enu(self) -> List:
        dic = {}
        for i, element in enumerate(self.nums):
            dif = self.target - element
            if dif not in dic:
                dic[element] = i
            else:
                return dic[dif], i


sol = Solution(List, Target)
print(sol.twoSum())
print(sol.twoSum_enu())
