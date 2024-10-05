class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        # breakdown problem: return the longest common prefix by its length. Find out the common prefix between each integer first, then find the max
        # maybe use two pointer to keep track
        # hashtable to store all possible prefix from the array 1. For each num in arr1 we break it digit by digit, store every prefix form by dividing it by 10. This way the hash table can contain all possible prefix value that could be a part of integer in arr2
        # for each num in arr2, we match with prefix store in the hash table

        arr1_prefixes = set()

        for val in arr1:
            while val not in arr1_prefixes and val > 0:
                arr1_prefixes.add(val)
                val //= 10 

        longest_prefixes = 0 

        for val in arr2:
            while val not in arr1_prefixes and val > 0:
                val //= 10 
            if val > 0:
                longest_prefixes = max(longest_prefixes, len(str(val)))
        return longest_prefixes
        
    # Time complexity: O(mlogM + nlongN) because it traverse through val in arr1 exactly once and then traverse through val in arr2  exactly once
    # Space complexity: O(log10M) which N is the length of arr1 to store the prefix 

        