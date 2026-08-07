class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for num in nums:
            if num - 1 in numSet:
                continue
            i = 0
            streak = 0
            while num + i in numSet:
                i +=1
                streak += 1
            longest = max(longest, streak)

        return longest
