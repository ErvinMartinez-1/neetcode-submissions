class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        n = len(position)
        for i in range(n):
            cars.append([position[i], speed[i]])
        
        cars.sort(reverse=True)

        stck = []
        for pos, speed in cars:
            if not stck:
                time = (target - pos) / speed
                stck.append(time)
                continue
            stckT = stck[-1]
            currT = (target - pos) / speed
            if currT > stckT:
                stck.append(currT)
                
        return len(stck)