class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts = {}

        for char in s:
            counts[char] = counts.get(char, 0) + 1
        
        for char in t:
            counts[char] = counts.get(char, 0) - 1
        
        print(counts.values())

        return all(value == 0 for value in counts.values())
