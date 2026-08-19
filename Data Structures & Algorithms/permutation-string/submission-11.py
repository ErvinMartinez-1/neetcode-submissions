class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2, = len(s1), len(s2)
        if n1 > n2:
            return False
        d1, d2 = {}, {}

        for i in range(n1):
            d1[s1[i]] = d1.get(s1[i], 0) + 1
            d2[s2[i]] = d2.get(s2[i], 0) + 1
        
        if d1 == d2:
            return True
        l = 0
        for r in range(n1, n2):
            d2[s2[r]] = d2.get(s2[r], 0) + 1
            d2[s2[l]] -= 1
            if d2[s2[l]] == 0:
                d2.pop(s2[l])
            l += 1

            if d1 == d2:
                return True
        
        return False


