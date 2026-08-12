class Solution:
    def binarySearch(self, left: int, right: int, nums: List[int], target: int) -> int:
        if left > right:
            return -1

        mid = right - ((right - left) // 2) 

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            return self.binarySearch(mid + 1, right, nums, target)
        else:
            return self.binarySearch(left, mid - 1, nums, target)

    def search(self, nums: List[int], target: int) -> int:
        return self.binarySearch(0, len(nums) - 1, nums, target)


            