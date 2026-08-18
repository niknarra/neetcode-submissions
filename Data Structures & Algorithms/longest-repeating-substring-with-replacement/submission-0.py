class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = {}
        left = right = 0
        res = maxF = 0

        while right < len(s):
            counts[s[right]] = counts.get(s[right], 0) + 1
            maxF = max(maxF, counts[s[right]])

            while (right-left + 1) - maxF > k:
                counts[s[left]] -= 1
                left += 1

            res = max(res, (right-left)+1)
            right += 1

        return res