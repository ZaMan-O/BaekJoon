#include <iostream>
#include <vector>
using namespace std;

struct set {
	int sung_gong_yeou_bu = 1;
	string str;
};
int main() {
	int tc;
	cin >> tc;
	vector<set> arr(tc);
	
	for (int i = 0;i < tc;i++) {
		cin >> arr[i].str;

		int top = -1;
		for (int ii = 0;ii < arr[i].str.length();ii++) {
			if (arr[i].str[ii] == '(') ++top;
			else if (top == -1) {
				arr[i].sung_gong_yeou_bu = 0;
				break;
			}
			else --top;
		}
		if (top != -1) arr[i].sung_gong_yeou_bu = 0;
	}
	
	for (int i = 0;i < tc;i++) {
		cout << (arr[i].sung_gong_yeou_bu ? "YES" : "NO") << "\n";
	}
}