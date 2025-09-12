#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

struct check {
	int checked = 0;
	int num;
};

bool compare(int a, int b) {
	return a < b;
}
int main() {
	int tc1, tc2;

	cin >> tc1;
	vector<int> arr(tc1);
	for (int i = 0;i < tc1;i++) {
		cin >> arr[i];
	}
	sort(arr.begin(), arr.end(), compare);

	cin >> tc2;
	vector<check> arr2(tc2);
	for (int i = 0;i < tc2;i++) {
		cin >> arr2[i].num;
		if (binary_search(arr.begin(), arr.end(), arr2[i].num)) arr2[i].checked = 1;
	}

	for (int i = 0;i < tc2;i++) {
		cout << arr2[i].checked << "\n";
	}
}