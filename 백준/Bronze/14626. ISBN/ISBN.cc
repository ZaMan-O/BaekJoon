#include <iostream>
#include <cstdlib>
using namespace std;
int main() {
	string str;
	int star_index;
	int sum = 0;
	cin >> str;
	for (int i = 0;i < 13;i++) {
		if (str[i] == '*') star_index = i;
		else {
			int n = str[i] - '0';
			if (i % 2 == 0) sum += n;
			else sum += n * 3;
		}
	} sum %= 10;
	if (sum == 0) cout << 0;
	else {
		if (star_index % 2 == 0) cout << 10 - sum;
		else cout << (sum * 3) % 10;
	}
}