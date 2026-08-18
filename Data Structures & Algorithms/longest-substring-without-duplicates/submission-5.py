class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left = right = 0
        res = 0

        while right < len(s):

            if s[right] in seen:
                while s[right] in seen:
                    seen.remove(s[left])
                    left += 1
            else:
                seen.add(s[right])
                res = max(res, len(seen))
                right += 1
        
        return res



