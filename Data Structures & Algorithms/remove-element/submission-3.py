class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        # As it doesn't matter what is left after k, we don't really have to swap
        # we just have to make sure val doesn't exist until kth element in the array
        # [3,2,2,3] can be [2,2,2,3] so the loop can be simple
        for num in nums:
            if num != val:
                # Only maintain last non value idx as k
                nums[k] = num
                # and swap if current idx is non value
                k += 1

        return k