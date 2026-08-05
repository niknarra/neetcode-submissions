class Solution {
public:
    // We first ^ to get the digits after a + b ignoring the carry
    // to get the carry, we do & and << by 1 as carry moves from right
    // This algo doesn't work in Python because of how Py treats ints
    int getSum(int a, int b) {
        while(b){
            int tmp = (a & b) << 1;
            a = a ^ b;
            b = tmp;
        }
        return a;
    }
};
