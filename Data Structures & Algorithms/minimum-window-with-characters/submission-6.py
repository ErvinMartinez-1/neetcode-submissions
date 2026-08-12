class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need, have = {}, {}

        for i in range(len(t)):
            need[t[i]] = need.get(t[i], 0)
            have[t[i]] = have.get(t[i], 0) + 1

        l = countN = 0
        countH = len(t)
        smallest = None

        for r in range(len(s)):
            if s[r] in need:
                need[s[r]] += 1
                if need[s[r]] <= have[s[r]]:
                    countN += 1
            while countN == countH:
                if smallest is None:
                    smallest = s[l : r + 1]
                else:
                    smallest = min(smallest, s[l : r + 1], key=len)
                if s[l] in need:
                    if need[s[l]] <= have[s[l]]:
                        countN -= 1
                    need[s[l]] -= 1
                l += 1

        return "" if smallest is None else smallest
                


