class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = collections.deque()

        for i in range(k):
            while q and nums[q[-1]] < nums[i]:
                q.pop()
            q.append(i)
        result = []
        result.append(nums[q[0]])
        l = 0
        for r in range(k, len(nums)):
            l += 1
            if q[0] < l:
                q.popleft()
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)
            result.append(nums[q[0]])
        return result