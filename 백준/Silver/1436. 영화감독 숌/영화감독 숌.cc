#include <iostream>
#include <string>
#include <vector>
#include <utility>
#include <cmath>
using namespace std;
int main() {
    int check = 0;
	int tc;
    
	int str;
	string str2;
    
	cin >> tc;
	for (str = 666;;str++) {
		str2 = to_string(str);
		if (str2.find("666") != -1) {
			++check;
			if (check == tc) {
				cout << str;
				break;
			}
		}
	}
}