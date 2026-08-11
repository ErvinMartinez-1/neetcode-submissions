class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        word = s.lower()
        while l < r:
            if word[l] == " " or not word[l].isalnum():
                l += 1
                continue
            if word[r] == " " or not word[r].isalnum():
                r -= 1
                continue
            if word[l] != word[r]:
                return False
            l += 1
            r -= 1

        return True
