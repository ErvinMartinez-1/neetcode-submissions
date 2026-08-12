class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        if n1 > n2:
            return False

        map1, map2 = {}, {}

        for i in range(n1):
            map1[s1[i]] = map1.get(s1[i], 0) + 1
            map2[s2[i]] = map2.get(s2[i], 0) + 1
        
        if map1 == map2:
            return True
        
        for i in range(n1, n2):
            map2[s2[i]] = map2.get(s2[i], 0) + 1
            map2[s2[i - n1]] -= 1
            if map2[s2[i - n1]] == 0:
                map2.pop(s2[i - n1])
            if map1 == map2:
                return True

        return False