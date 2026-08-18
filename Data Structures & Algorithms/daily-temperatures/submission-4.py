class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stck = []
        result = [0] * len(temperatures)

        for i in range(len(temperatures) - 1, -1, -1):
            if not stck:
                stck.append([i, temperatures[i]])
                continue
            while stck and stck[-1][1] <= temperatures[i]:
                stck.pop()
            if stck:
                difference = stck[-1][0] - i
                result[i] = difference
            
            stck.append([i, temperatures[i]])
        
        return result
                        
