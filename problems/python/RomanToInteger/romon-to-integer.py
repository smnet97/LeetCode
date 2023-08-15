class Solution:
    def romanToInt(self, s: str) -> int: # LIX
        roman_numbers = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000}
        
        value = 0
        i = 0
        while i < len(s) - 1:
            
            if roman_numbers[s[i]] >= roman_numbers[s[i + 1]]:
                value += roman_numbers[s[i]]
                i += 1
            else:
                value += roman_numbers[s[i + 1]] - roman_numbers[s[i]]
                i += 2
                
        if i == len(s) - 1:
            value += roman_numbers[s[i]]
        
        return value
    

object1 = Solution()
print(object1.romanToInt('LIX'))