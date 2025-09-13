#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

bool compare(int a, int b) {
	return a < b;
}

struct set {
	int data;
	int amount;
};

int main() {
	int tc;
	cin >> tc;
	vector<int> arr1(tc);
	for (int i = 0;i < tc;i++) {
		cin >> arr1[i];
	}
	sort(arr1.begin(), arr1.end(), compare);

	int tc2;
	cin >> tc2;
	vector<set> arr2(tc2);
	for (int i = 0;i < tc2;i++) {
		cin >> arr2[i].data;
		auto index = equal_range(arr1.begin(), arr1.end(), arr2[i].data);
		arr2[i].amount = index.second - index.first;
	}
	for (int i = 0;i < tc2;i++) {
		cout << arr2[i].amount << "\n";
	}
}