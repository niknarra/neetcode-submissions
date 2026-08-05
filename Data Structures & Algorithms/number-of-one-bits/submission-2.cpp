class Solution {
public:
    int hammingWeight(uint32_t n) {
        int count = 0;
        while(n){
            // Difference in bits b/w n and n-1 is a single 1-bit (LSB)
            // When we 1 & 0 -> 0 -> We're removing a 1-bit everytime the loop runs
            // The loop runs as long as a 1-bit exists
            n = n & (n-1);
            count += 1;
        }
        return count;
    }
};
