class Solution:
    def removeElement(self, nums: list, val: int) -> int:
        
        t = 0
        for i in range(len(nums)):
            if val != nums[i]:
                nums[t] = nums[i]
                t += 1
        return t
    
s = Solution()
s.removeElement([3,2,2,3], 3)