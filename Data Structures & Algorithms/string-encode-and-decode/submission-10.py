class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = []

        for s in strs:
            encoded.append(str(len(s)))
            encoded.append('#')
            encoded.append(s)
        
        return ''.join(encoded)

    def decode(self, s: str) -> List[str]:
        decoded = []
        curr = 0

        while curr < len(s):
            j = curr

            while s[j] != '#':
                j += 1
                
            currLen = int(s[curr:j])
            curr = j + 1

            decoded.append(s[curr:curr+currLen])

            curr += currLen

        return decoded