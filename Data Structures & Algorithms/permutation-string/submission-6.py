class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
            n1, n2 =  len(s1), len(s2)
            if n1 > n2:
                return False

            dict1, dict2 = {}, {}

            for i in range(n1):
                dict1[s1[i]] = dict1.get(s1[i], 0) + 1
                dict2[s2[i]] = dict2.get(s2[i], 0) + 1
            
            if dict1 == dict2:
                return True

            l = 0
            for r in range(n1, n2):
                dict2[s2[l]] -= 1
                if dict2[s2[l]] == 0:
                    dict2.pop(s2[l])
                l += 1

                dict2[s2[r]] = dict2.get(s2[r], 0) + 1
                if dict1 == dict2:
                    return True
            
            return False

            
            



        