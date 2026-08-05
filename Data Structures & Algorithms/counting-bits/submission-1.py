class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0] * (n+1)
        i = 1

        while i <= n:
            res[i] = res[i & (i-1)] + 1
            i += 1

        return res