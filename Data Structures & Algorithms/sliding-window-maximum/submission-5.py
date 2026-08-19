class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = collections.deque()

        for i in range(k):
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()

            dq.append(i)
        
        result = []
        result.append(nums[dq[0]])
        l = 0

        for r in range(k, len(nums)):
            l += 1
            if dq[0] < l:
                dq.popleft()  
            while dq and nums[dq[-1]] < nums[r]:
                dq.pop()

            dq.append(r)
            result.append(nums[dq[0]])
        
        return result