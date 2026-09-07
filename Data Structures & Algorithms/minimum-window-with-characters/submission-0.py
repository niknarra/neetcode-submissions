class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # If s is shorter than t, it's impossible to contain all characters
        if len(s) < len(t):
            return ""

        # Frequency map of characters we NEED from t
        existing = defaultdict(int)

        # Frequency map of characters currently inside our window
        seen = defaultdict(int)

        res = ""

        # Build the frequency requirements from t
        #
        # Example:
        # t = "AABC"
        # existing = {A: 2, B: 1, C: 1}
        for char in t:
            existing[char] += 1

        left = right = 0

        # "have" = number of distinct characters whose required
        # frequency has been satisfied in the current window
        #
        # "need" = number of distinct characters we need to satisfy
        #
        # Example:
        # t = "AABC"
        # need = 3  -> A, B, C
        have = 0
        need = len(existing)

        # Length of the best window we've found
        resLen = float("inf")

        while right < len(s):
            char = s[right]

            # Only care about characters that are actually required by t
            if char in existing:
                seen[char] += 1

                # We just reached the required frequency for this character
                #
                # Example:
                # existing[A] = 2
                # seen[A] goes from 1 -> 2
                # Therefore A is now "satisfied"
                if seen[char] == existing[char]:
                    have += 1

            # If we have all required characters,
            # try shrinking the window from the left.
            #
            # IMPORTANT:
            # This is a VARIABLE-sized window.
            # We keep shrinking while the window is valid.
            while have == need:

                # Current window contains everything we need,
                # so check whether it's the smallest one we've found.
                currLen = right - left + 1

                if currLen < resLen:
                    resLen = currLen
                    res = s[left:right + 1]

                # We're about to remove the leftmost character
                leftChar = s[left]

                if leftChar in existing:
                    seen[leftChar] -= 1

                    # If removing this character causes us to have
                    # fewer than the required amount, the window
                    # is no longer valid.
                    #
                    # Example:
                    # need A = 2
                    # seen A = 2
                    # remove A -> seen A = 1
                    # Now A is no longer satisfied.
                    if seen[leftChar] < existing[leftChar]:
                        have -= 1

                # Move the left side of the window forward
                left += 1

            # Expand the window by moving right
            right += 1

        return res
