class Solution:
    def removeElement(self, nums: list, val: int) -> int:
        if len(nums) == 0: return 0
        elif len(nums) == 1: return 1
        
        t = 0
        for i in range(len(nums)):
            if val != nums[i]:
                nums[t] = nums[i]
                t += 1
        return t
    
s = Solution()
s.removeElement([3,2,2,3], 3)