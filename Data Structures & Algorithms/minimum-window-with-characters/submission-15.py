class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n1, n2 = len(t), len(s)
        if n1 > n2:
            return ""

        d1, d2 = {}, {}
        for i in range(n1):
            d1[t[i]] = d1.get(t[i], 0) + 1
            d2[t[i]] = d2.get(t[i], 0)

        l = numHave = 0
        numNeed = n1
        minRange = [-1, -1]
        minLen = float("infinity")
        for r in range(n2):
            if s[r] in d1:
                d2[s[r]] += 1
                if d2[s[r]] <= d1[s[r]]:
                    numHave += 1
            while numHave == numNeed:
                if r - l + 1 < minLen:
                    minLen = r - l + 1
                    minRange = [l, r]
                if s[l] in d1:
                    d2[s[l]] -= 1
                    if d2[s[l]] < d1[s[l]]:
                        numHave -= 1
                l += 1
        
        l, r = minRange
        return "" if minLen == float("infinity") else s[l: r+1]