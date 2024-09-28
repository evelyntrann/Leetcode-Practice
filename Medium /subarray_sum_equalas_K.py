class Solution
    def subarraySum (nums, k):
        count = 0
        sum_val = 0
        sum_map = {0: 1}

        for num in nums:
            sum_val += num
            if (sum_val - k) in sum_map:
                count += sum_map[sum_val - k]
            sum_map[sum_val] = sum_map.get(sum_val, 0) + 1

        return count

                