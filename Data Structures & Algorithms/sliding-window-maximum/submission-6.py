class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = deque()
        res = []

        left = right = 0

        while right < len(nums):
            # Remove smaller values from the back.
            # They can never become the maximum while nums[right]
            # is still in the window.
            while ans and ans[-1][0] < nums[right]:
                ans.pop()
            
            # Store both value AND index
            ans.append((nums[right], right))

            if (right-left) + 1 >= k:
                # Remove elements that have fallen outside the window
                if ans[0][1] < left:
                    ans.popleft()
                
                # Front always contains the largest value
                res.append(ans[0][0])
                
                left += 1

            right += 1

        return res
