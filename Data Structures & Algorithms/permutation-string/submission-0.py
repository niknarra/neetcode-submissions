class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        
        left = right = 0
        existing = {}
        seen = {}

        for char in s1:
            existing[char] = existing.get(char, 0) + 1
        
        while right < len(s2):
            if s2[right] in existing:
                seen[s2[right]] = seen.get(s2[right], 0) + 1

            if right - left + 1 > len(s1):
                if s2[left] in existing:
                    seen[s2[left]] -= 1
                
                    if seen[s2[left]] == 0:
                        del seen[s2[left]]
                
                left += 1
            
            if seen == existing:
                return True
            
            right += 1
        
        return False