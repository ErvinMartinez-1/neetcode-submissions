class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need, have = {}, {}
        if len(s) < len(t):
            return ""
        for i in range(len(t)):
            need[t[i]] = need.get(t[i], 0) + 1
        
        l = numHave = 0
        numNeed = len(t)
        indexes = [-1, -1]
        minLength = float("infinity")
        for r in range(len(s)):
            if s[r] in need:
                have[s[r]] = have.get(s[r], 0) + 1
                if have[s[r]] <= need[s[r]]:
                    numHave += 1
            while numHave == numNeed:
                length = r - l + 1
                if length < minLength:
                    indexes = [l, r+1]
                    minLength = length
                if s[l] in need:
                    have[s[l]] -= 1
                    if have[s[l]] < need[s[l]]:
                        numHave -= 1
                l += 1
        
        l,r = indexes[0], indexes[1]
        return "" if minLength == float("infinity") else s[l:r]


        