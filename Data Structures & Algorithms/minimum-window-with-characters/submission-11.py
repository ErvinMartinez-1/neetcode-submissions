class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need, have = {}, {}

        if len(t) > len(s):
            return ""

        for i in range(len(t)):
            need[t[i]] = need.get(t[i], 0) + 1
            have[t[i]] = have.get(t[i], 0)

        numNeed = len(t)
        numHave = l = 0
        shortest = None

        for r in range(len(s)):
            if s[r] in need:
                have[s[r]] += 1
                if have[s[r]] <= need[s[r]]:
                    numHave += 1
            
            while numHave == numNeed:
                if shortest is None:
                    shortest = s[l: r + 1]
                else:
                    shortest = min(shortest, s[l: r + 1], key=len)
                if s[l] in need:
                    if have[s[l]] <= need[s[l]]:
                        numHave -= 1
                    have[s[l]] -= 1
                l += 1
        
        return "" if shortest is None else shortest

        