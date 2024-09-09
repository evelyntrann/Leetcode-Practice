class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        curr_sum = 0

        # Iterate through the array, starting from the second element
        for i in range(len(nums)):
            curr_sum = max(curr_sum, 0) + nums[i] #help us to decide to extend the current sum or start fresh at the new one.
            #case 1: curr_sum + nums[i] (extend)
            #case 2: 0 + nums[i] (start a new one)
            max_sum = max(curr_sum, max_sum)
        return max_sum
        