class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        def isValid(left, right):
            while left < right:
                if s[left].lower() == s[right].lower():
                    left += 1
                    right -= 1
                else:
                    return False
            
            return True

        left, right = 0, len(s) - 1

        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return isValid(left+1, right) or isValid(left, right-1)
        
        return True

