class Solution:
    def countBits(self, n: int) -> List[int]:
        def counterr(curr):
            count = 0
            while curr:
                curr = curr & (curr - 1)
                count += 1
            return count

        res = [0]
        i = 1
        while i<=n:
            res.append(counterr(i))
            i += 1

        return res