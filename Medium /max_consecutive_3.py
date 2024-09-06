class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        if nums is None: 
            return 0 
        left = 0 #use sliding windows left = 0 and right = 0
        res = float('-inf')
        zero = 0 

        for right in range(len(nums)):
            if nums[right] == 1: #right = 1 so we continue going by 1
                pass
            else:
                zero += 1 #zero + 1
            while zero > k: #keep track with the integer we have
                if nums[left] == 0: 
                    zero -= 1
                left += 1 #move one step to make sure zero count not exceed k integer
            res = max(res, right - left + 1)
        return res
        