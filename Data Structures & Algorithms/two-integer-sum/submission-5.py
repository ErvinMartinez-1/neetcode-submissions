class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hMap = {}

        for i in range(len(nums)):
            needed = target - nums[i]
            if needed in hMap:
                return [hMap[needed], i]
            else:
                hMap[nums[i]] = i