class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        curr = 0
        non_val = len(nums) - 1

        while curr <= non_val:
            if nums[curr] == val:
                while curr <= non_val and nums[non_val] == val:
                    non_val -= 1

                if curr <= non_val:
                    nums[curr], nums[non_val] = nums[non_val], nums[curr]
                    non_val -= 1

            else:
                curr += 1

        return non_val + 1