class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        n1, n2 = len(t), len(s)
        need, have = {}, {}
        for i in range(n1):
            need[t[i]] = need.get(t[i], 0) + 1
        
        l = 0
        numHave, numNeed = 0, n1
        shortest = [-1, -1]
        smallest = float("infinity")
        for r in range(n2):
            if s[r] in need:
                have[s[r]] = have.get(s[r], 0) + 1
                if have[s[r]] <= need[s[r]]:
                    numHave += 1
            while numHave == numNeed:
                length = r - l + 1
                if length < smallest:
                    smallest = length
                    shortest = [l, r+1]
                if s[l] in need:
                    have[s[l]] -= 1
                    if have[s[l]] < need[s[l]]:
                        numHave -= 1
                l += 1
        l, r = shortest[0], shortest[1]
        return s[l:r]

