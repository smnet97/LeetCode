class Solution:
    def twoSum(self, nums: list, target: int) -> list:
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if nums[i] + nums[j] == target and i != j:
                    return [i, j]
                elif i == len(nums) and j == len(nums):
                    return []

obj = Solution()
print(obj.twoSum([3,2,4], 6))