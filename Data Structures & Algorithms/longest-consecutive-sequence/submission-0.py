class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest_len = 0

        for num in nums:
            if num - 1 in numSet:
                continue
            i = 0
            streak = 0
            while num + i in numSet:
                streak += 1
                i += 1
            longest_len = max(longest_len, streak)

        return longest_len