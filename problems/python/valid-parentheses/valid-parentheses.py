class Solution:
    def isValid(self, s: str) -> bool:
        my_dict = {
            '(': ')', 
            '{': '}',
            '[': ']'
            }
        tmp = []
        for char in s:
            if char in my_dict.keys():
                tmp.append(char)
            elif tmp and char == my_dict[tmp[-1]]:
                tmp.pop()
            else:
                return False
            
        return len(tmp) == 0