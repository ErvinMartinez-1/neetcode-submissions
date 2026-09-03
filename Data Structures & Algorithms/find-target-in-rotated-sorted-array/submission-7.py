class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            m = (l+r) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        minIndex = l
        if minIndex == 0:
            l, r = 0, len(nums) - 1
        elif target >= nums[0] and target <= nums[minIndex - 1]:
            l, r = 0, minIndex - 1
        else:
            l, r = minIndex, len(nums) - 1

        while l <= r:
            m = (l+r) // 2
            if nums[m] == target:
                return m
            if nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        return -1