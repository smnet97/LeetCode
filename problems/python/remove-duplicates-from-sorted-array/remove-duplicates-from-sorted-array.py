class Solution:
    def removeDuplicates(self, nums: list) -> int:
        if len(nums) == 0: return 0
        elif len(nums) == 1: return 1
        
        t = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[t] = nums[i]
                t += 1
        return t
    
s = Solution()
s.removeDuplicates([0,0,1,1,1,2,2,3,3,4])