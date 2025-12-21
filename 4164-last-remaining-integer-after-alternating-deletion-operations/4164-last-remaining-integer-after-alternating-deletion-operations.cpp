class Solution {
public:
    long long lastInteger(long long n) {
        long long start = 1, end = n, step = 1;
        unsigned long long m;
        for (m = (unsigned long long) n; m != (1 | (1LL << (bit_width(m) - 1))); m -= m >> 1)
            tie(start, end, step) = make_tuple(end - ((m & 1) ? 0: step), start, -2 * step);
            
        return bit_width(m) & 1 ? start : end;
    }
};