import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_lowered = s.lower()
        s_valid = re.sub(r'[^a-zA-Z0-9]', '', s_lowered)
        newS = s_valid.replace(" ", "")

        l = 0
        r = len(newS) - 1
        while l < r:
            if newS[l] != newS[r]:
                return False
            else:
                l = l + 1
                r = r - 1
        return True