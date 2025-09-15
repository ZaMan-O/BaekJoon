#include <iostream>
#include <cmath>
using namespace std;

int main() {
	int num;
	cin >> num;
	int log_num = (int)log10(num) + 1;

	for (int i = num - log_num * 9;i <= num - log_num;i++) {
		if (i == num - log_num) {
			cout << 0;
			break;
		}
		int temp = i;
		int temp2 = i;
		for (int ii = 0;ii < log_num;ii++) {
			temp += (temp2 % 10);
			temp2 = temp2 / 10;
		}
		if (temp == num) { cout << i; break; }
	}
}