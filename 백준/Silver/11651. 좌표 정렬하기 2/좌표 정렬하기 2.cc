#include <iostream>
#include <algorithm>
#include <vector>
#include <utility>
using namespace std;
bool compare(pair<int, int> a, pair<int, int> b) {
	if (a.second == b.second) return a.first < b.first;
	return a.second < b.second;
}
int main() {
	int tc;
	cin >> tc;
	vector<pair<int, int>> arr(tc);
	for (int i = 0;i < tc;i++) {
		cin >> arr[i].first >> arr[i].second;
	}
	sort(arr.begin(), arr.end(), compare);
	for (int i = 0;i < tc;i++) {
		cout << arr[i].first << " " << arr[i].second << "\n";
	}
}