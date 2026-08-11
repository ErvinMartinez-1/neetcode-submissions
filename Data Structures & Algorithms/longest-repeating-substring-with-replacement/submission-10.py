class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        l, longest = 0, 0

        for r in range(len(s)):
            freq[s[r]] = freq.get(s[r], 0) + 1
            changes = (r - l + 1) - max(freq.values())
            while changes > k:
                freq[s[l]] -= 1
                l += 1
                changes = (r - l + 1) - max(freq.values())
            longest = max(longest, r - l + 1)

            
        return longest