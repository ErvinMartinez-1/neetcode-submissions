class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hMap = {}

        for num in nums:
            hMap[num] = hMap.get(num, 0) + 1

        return max(hMap, key=hMap.get)