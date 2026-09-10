class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        
        existing = defaultdict(int)
        seen = defaultdict(int)

        for char in t:
            existing[char] += 1
        
        left = right = 0
        have = 0
        need = len(existing)
        resLen = float('inf')
        res = ""

        while right < len(s):
            if s[right] in existing:
                seen[s[right]] += 1
            
                if seen[s[right]] == existing[s[right]]:
                    have += 1
            
            while have == need:
                currLen = (right-left) + 1
                if currLen < resLen:
                    res = s[left:right+1]
                    resLen = currLen
                
                if s[left] in existing:
                    seen[s[left]] -= 1

                    if seen[s[left]] < existing[s[left]]:
                        have -= 1
                
                left += 1
            
            right += 1
        
        return res

