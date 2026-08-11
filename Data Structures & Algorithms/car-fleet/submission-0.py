class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        carPair = []
        n = len(position)

        for i in range(n):
            carPair.append([position[i], speed[i]])
        
        cars = sorted(carPair, reverse=True)

        stck = []
        for pos, speed in cars:
            if not stck:
                stck.append([pos, speed])
                
            stckInterval = (target - stck[-1][0]) / stck[-1][1]
            currInterval = (target - pos) / speed

            if currInterval <= stckInterval:
                continue
            else:
                stck.append([pos, speed])
        
        return len(stck)

        