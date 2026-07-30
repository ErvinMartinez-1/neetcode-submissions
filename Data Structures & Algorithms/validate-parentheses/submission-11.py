class Solution:
    def isValid(self, s: str) -> bool:
        stck = []
        key = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for c in s:
            if c not in key:
                stck.append(c)
            else:
                if stck and stck[-1] == key[c]:
                    stck.pop()
                else: 
                    return False

        return True if not stck else False
                    
            