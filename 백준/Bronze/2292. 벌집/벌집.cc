#include <iostream>
using namespace std;

int main() {
	int num, multi = 6;
	cin >> num;
	if (num == 1) {
		cout << 1;
	}
	else {
		for (int i = 2;1;i++) {
			if ((num - 2) / multi == 0) { cout << i; break; }
			multi += 6 * i;
		}
	}
	
}