class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0 
        size = len(height)
        left_max, right_max = [0] * size, [0] * size
        left_max[0] = height[0]
        for i in range(1, size):
            left_max[i] = max(left_max[i -1], height[i])
        right_max[size-1] = height[size-1]
        for i in range(size -2, -1, -1):
            right_max[i] = max(height[i], right_max[i+1])
        for i in range(1, size - 1):
            ans += min(left_max[i], right_max[i]) - height[i]
        return ans

        
        