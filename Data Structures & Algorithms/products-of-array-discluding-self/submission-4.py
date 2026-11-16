class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        product = 1
        for num in nums:
            prefix.append(product)
            product *= num

        postfix = deque()
        product = 1
        for num in range(len(nums) - 1, -1, -1):
            postfix.appendleft(product)
            product *= nums[num]
        
        answer = []
        for n in range(len(nums)):
            answer.append(prefix[n] * postfix[n])
        
        return answer
