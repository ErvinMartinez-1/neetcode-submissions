class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n1, n2 = len(s), len(t)
        if n2 > n1:
            return ""
        
        need, have = {}, {}
        for i in range(n2):
            need[t[i]] = need.get(t[i], 0) + 1
            have[t[i]] = have.get(t[i], 0)

        numHave, numNeed = 0, len(t)
        indexes = [-1, -1]
        shortest = float("infinity")
        l = 0
        for r in range(n1):
            if s[r] in need:
                have[s[r]] += 1
                if have[s[r]] <= need[s[r]]:
                    numHave += 1
            while numHave == numNeed:
                if shortest > r - l + 1:
                    shortest = r - l + 1
                    indexes = [l, r+1]
                if s[l] in need:
                    have[s[l]] -= 1
                    if have[s[l]] < need[s[l]]:
                        numHave -= 1
                l += 1

        l, r = indexes[0], indexes[1]
        return "" if shortest == float("infinity") else s[l:r]