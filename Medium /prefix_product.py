class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        length = len(nums)
        answer = [1] * length #initial the answer array with 1
 
        left = 1 #traverse the left handside of the current value
        for i in range(length): 
            answer[i] = left 
            left *= nums[i] #update the left value

        right = 1 #traverse the right handside of the current value
        for i in reversed(range(length)):
            answer[i] = answer[i] * right
            right *= nums[i]

        return answer
        
        #Time complexity: O(N) where N is the number of elements in the input array