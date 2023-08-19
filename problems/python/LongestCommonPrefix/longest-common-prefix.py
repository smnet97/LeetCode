class Solution:
    def longestCommonPrefix(self, strs:list) ->str:
        if not strs:
            return ""
        short_str = min(strs,key=len)
        for index, char in enumerate(short_str):
            for other in strs:
                if other[index] != char:
                    return short_str[:index]
        return short_str
     


