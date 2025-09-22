#include <iostream>
#include <cmath>
using namespace std;
int main() {
    int tc;
    cin >> tc;
    int num = 0, ii = 0;
    for (int i = 0;i <= tc;i++) {
        int now_pow = 0;
        if (num == 0) ++num;
        else {
            num *= i;
            while (1) {
                if (num % (int)pow(10, now_pow + 1) != 0) break;
                ++ii; ++now_pow;
            }
            num = (num % (int)pow(10, now_pow + (int)log10(tc) + 1)) / (int)pow(10, now_pow);
        }
    } cout << ii;
}