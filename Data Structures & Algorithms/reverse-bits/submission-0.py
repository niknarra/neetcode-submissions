class Solution:
    # We're using the same reverse an integer algo
    # but with base as 2 rather than 10
    def reverseBits(self, n: int) -> int:
        result = 0
        for i in range(32):
            bit = n & 1 # Getting the LSB or the first bit from right
            # Move result's MSB to left by 1
            # and add the extracted bit to the end
            result = (result << 1) | bit
            n >>= 1 # Drop the LSB as it's already processed
        
        return result