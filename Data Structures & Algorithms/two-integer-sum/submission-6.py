class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hMap = {}

        for i, num in enumerate(nums):
            print(i, num)
            difference = target - num
            if difference in hMap:
                return [hMap[difference], i]
            hMap[num] = i 
        