class Solution {
public:
    vector<int> countBits(int n) {
        vector<int> res(n+1);

        for(int i=1; i<=n; i++){
            // setBits(i) = setBits(i & (i - 1)) + 1
            // i & (i - 1) removes the rightmost set bit from i.
            // So it has exactly one fewer set bit than i.
            // Therefore, the number of set bits in i is:
            // (set bits after removing one set bit) + 1.
            res[i] = res[i & (i-1)] + 1;
        }
        return res;
    }
};
