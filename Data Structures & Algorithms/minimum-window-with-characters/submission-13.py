class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n1, n2 = len(t), len(s)
        if n1 > n2:
            return ""
        d1, d2 = {}, {}
        shortest = None
        for i in range(n1):
            d1[t[i]] = d1.get(t[i], 0) + 1
            d2[t[i]] = d2.get(t[i], 0)

        l =  numHave = 0
        numNeed = n1
        for r in range(n2):
            if s[r] in d1:
                d2[s[r]] += 1
                if d2[s[r]] <= d1[s[r]]:
                    numHave += 1
            while numHave == numNeed:
                if shortest is None:
                    shortest = s[l : r+1]
                else:
                    shortest = min(shortest, s[l: r+1], key=len)
                if s[l] in d1:
                    d2[s[l]] -= 1
                    if d2[s[l]] < d1[s[l]]:
                        numHave -= 1
                l += 1
        return "" if shortest is None else shortest