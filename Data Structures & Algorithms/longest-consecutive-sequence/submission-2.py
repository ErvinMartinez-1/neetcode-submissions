class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers = set(nums)
        longest = 0
        for num in nums:
            if num - 1 in numbers:
                continue
            i = 0
            while num + i in numbers:
                i += 1
            longest = max(longest, i)
        
        return longest
            