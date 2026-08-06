class Solution {
public:
    int smallestNumber(int n, int t) {
        while (true){
            int num = n;
            int prod = 1;
            while (num > 0){
                int digit = num % 10;
                prod *= digit;
                num /= 10;
            }
            if (prod % t == 0) return n;
            n++;
        }
    }
};