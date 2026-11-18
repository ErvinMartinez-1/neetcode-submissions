class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        l = longest = 0
        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            currLen = r - l + 1
            longest = max(longest, currLen)
        
        return longest