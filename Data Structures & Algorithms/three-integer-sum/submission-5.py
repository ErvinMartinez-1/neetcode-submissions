class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        seen = set()
        result = []
        for i in range(n - 2):
            if nums[i] > 0:
                break 
                
            j = i + 1
            k = n - 1
            while j < k:
                if nums[i] + nums[j] + nums[k] == 0 and not (i,j,k) in seen:
                    if not [nums[i], nums[j], nums[k]] in result:
                        result.append([nums[i], nums[j], nums[k]])

                    seen.add((i, j, k))
                    j += 1
                    continue
                if nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                else:
                    j += 1
        
        return result
