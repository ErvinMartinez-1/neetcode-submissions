class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
            temps = []
            for i, temp in enumerate(temperatures):
                temps.append([i, temp])
            
            stck = []
            result = [0] * len(temps)
            for i, temp in temps:
                if not stck:
                    stck.append([i, temp])
                while stck and stck[-1][1] < temp:
                    length = i - stck[-1][0]
                    result[stck[-1][0]] = length
                    stck.pop()
                stck.append([i, temp])

            return result