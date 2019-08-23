nums = [3,2,4,15,65,231,11,20]
target = 31

class Solution_1:
	def twoSum(self, nums, target):
		for inde_1,x in enumerate(nums):
			for inde_2,y in enumerate(nums):
				if x+y == target and inde_1 != inde_2:
					return([inde_1,inde_2])


class Solution_2:
	def twoSum(self, nums, target):
		dic = {}
		for i,x in enumerate(nums):
			dif = target - x
			if dif not in dic:
				dic[x] = i
			else:
				return [i,dic[dif]]

solution = Solution_2()
print(solution.twoSum(nums,target))
