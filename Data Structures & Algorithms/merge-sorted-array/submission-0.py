class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # We fill array1 from right->left i.e., Largest element -> Smallest element
        # TC: O(n); SC: O(1)

        zeroMax = len(nums1) - 1 # -> Tracks the index to put an element
        nums1FilledMax = m - 1 # -> Tracks the last filled/non-0 element in nums1
        nums2FilledMax = len(nums2) - 1 #-> Tracks the last element in nums2

        # While both arrays have elements
        while nums2FilledMax >= 0 and nums1FilledMax >= 0:
            if nums1[nums1FilledMax] >= nums2[nums2FilledMax]:
                nums1[zeroMax] = nums1[nums1FilledMax]
                nums1FilledMax -= 1

            else:
                nums1[zeroMax] = nums2[nums2FilledMax]
                nums2FilledMax -= 1

            zeroMax -= 1
        
        # We only need to check if nums2 has elements because nums1 is already sorted in ascending order
        # we don't need to sort what is already sorted
        while nums2FilledMax >= 0:
            nums1[zeroMax] = nums2[nums2FilledMax]
            nums2FilledMax -= 1
            zeroMax -= 1