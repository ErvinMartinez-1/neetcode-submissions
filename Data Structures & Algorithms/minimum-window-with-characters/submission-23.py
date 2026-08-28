class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        need, have = {}, {}

        for i in range(len(t)):
            need[t[i]] = need.get(t[i], 0) + 1
            have[t[i]] = have.get(t[i],0)
        
        numNeed = len(t)
        numHave = 0
        smallest = float("infinity")
        indexes = [0, 0]
        l = 0

        for r in range(len(s)):
            if s[r] in need:
                have[s[r]] += 1
                if have[s[r]] <= need[s[r]]:
                    numHave += 1
            while numHave == numNeed:
                length = r - l + 1
                if length < smallest:
                    smallest = r - l + 1
                    indexes = [l, r+1]
                if s[l] in need:
                    have[s[l]] -= 1
                    if have[s[l]] < need[s[l]]:
                        numHave -= 1
                l += 1
        
        left, right =  indexes[0], indexes[1]
        
        return "" if smallest == float("infinity") else s[left:right]

