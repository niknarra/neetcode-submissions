class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        res = 0

        while low <= high:
            count = 0
            mid = (low+high)//2

            for pile in piles:
                count += math.ceil(pile/mid)
                print(count, mid)
            
            if count <= h:
                res = mid
                high = mid - 1
            
            elif count > h:
                low = mid + 1
        
        return res
        
        