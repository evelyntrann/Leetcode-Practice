class Solution
    def countSubstring(self, s: str) -> int:
        count = 0 # we set count = 0 to keep track with the capacity of s 
        for i in range(len(s)):
            left = right = i # we set left and right at the start
            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1 #increase count by one if two pointer have the same value
                left -= 1 #decrease left by one
                right += 1
            #this will compare between two consecutive number 
            left = i 
            right = i + 1 
            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1 
        return count 