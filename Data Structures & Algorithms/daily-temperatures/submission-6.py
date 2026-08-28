class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)

        stck = []

        for i in range(len(temperatures) - 1, -1, -1):
            while stck and temperatures[stck[-1]] <= temperatures[i]:
                stck.pop()
            if not stck:
                stck.append(i)
                continue
            result[i] = stck[-1] - i
            stck.append(i)
        
        return result
            