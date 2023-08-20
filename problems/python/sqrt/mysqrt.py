class Solution:
    def mySqrt(self, x: int) -> int:
        t = x
        while not t * t - x < 1:
            t = (t + x / t) / 2
            
        return int(t)
                
                
s = Solution()
s.mySqrt(12)
                