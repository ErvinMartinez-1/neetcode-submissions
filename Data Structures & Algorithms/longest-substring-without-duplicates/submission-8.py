class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hSet = set()
        l = 0
        maxLen = 0
        for r in range(len(s)):
            while s[r] in hSet and l < r:
                hSet.remove(s[l])
                l += 1
            hSet.add(s[r])
            currLen = r - l + 1
            maxLen = max(maxLen, currLen)
        
        return maxLen
            

