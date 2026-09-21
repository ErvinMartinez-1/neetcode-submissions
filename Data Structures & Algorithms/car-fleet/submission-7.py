class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        for i in range(len(position)):
            cars.append((position[i], speed[i]))
        
        cars.sort(reverse=True)
        stck = []
        for pos, speed in cars:
            time = (target - pos) / speed
            if not stck:
                stck.append(time)
                continue
            if time > stck[-1]:
                stck.append(time)
        
        return len(stck)