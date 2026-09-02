class TimeMap:

    def __init__(self):
        self.tMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if not key in self.tMap:
            self.tMap[key] = self.tMap.get(key, [])
        
        self.tMap[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.tMap:
            return ""
        values = self.tMap[key]
        l, r = 0, len(values) - 1
        answer = ""
        index = -1
        while l <= r:
            m = (l+r) // 2
            if values[m][0] <= timestamp and index < m:
                answer = values[m][1]
                index = m
                l = m + 1
            else:
                r = m - 1
        return answer


        
            
            