class Solution:
    def longestPalindrome(self, s: str) -> str:
        #palindromic substring: 121 232 454
        # using two Pointer technique
        # differentiate between odd len string and even len string
        if len(s) == 0 and len(s) == 1: 
            return s 
        # two pointer to check if this is a palindrome or not
        def check(i, j):
            left = i
            right = j - 1
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True
        
        for end in range(len(s), 0, -1):
            for start in range(len(s) - end + 1):
                if check(start, start + end):
                    return s[start:start + end]     
        return ""


        


        





        


        