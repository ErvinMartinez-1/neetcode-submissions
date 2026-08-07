class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)

        multiplier = 1
        for i in range(0, len(nums)):
            output[i] *= multiplier
            multiplier *= nums[i]

        multiplier = 1
        for i in range(len(nums) - 1, -1, -1):
            output[i] *= multiplier
            multiplier *= nums[i]

        return output


