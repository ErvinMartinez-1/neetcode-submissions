class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        n = len(position)

        for i in range(n):
            cars.append([position[i], speed[i]])
        
        cars.sort(reverse=True)
        stck = []

        for p, s in cars:
            time = (target - p) / s
            if not stck:
                time = (target - p) / s
                stck.append(time)
                continue
            if time > stck[-1]:
                stck.append(time)
        
        return len(stck)
            