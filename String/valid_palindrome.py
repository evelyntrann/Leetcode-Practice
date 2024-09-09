class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 0 or len(s) == 1:
            return True #because " " or "a" read the same both backward and forward 
        s = ''.join(char.lower() for char in s if char.isalnum())
        left = 0 
        right = len(s) - 1

        while left <= right:
            if s[left] != s[right]:
                return False 
            left += 1
            right -= 1
        return True

                
                
        