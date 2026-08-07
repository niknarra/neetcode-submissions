class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        start = 0
        end = len(s) - 1

        while start < end:
            if s[start].isalnum() and s[end].isalnum():
                if s[start] != s[end]:
                    return False
                start += 1
                end -= 1
            elif not s[start].isalnum():
                start += 1
            elif not s[end].isalnum():
                end -= 1
        
        return True