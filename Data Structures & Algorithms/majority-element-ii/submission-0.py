class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counts = {}
        n = len(nums)
        res = []

        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        
        for key, value in counts.items():
            if value > (n//3):
                res.append(key)

        return res