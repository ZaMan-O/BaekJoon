#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <utility>
using namespace std;
bool compare(pair<int, int> a, pair<int, int> b) {
	return a.first > b.first;
}
bool compare2(int a, int b) {
	return a > b;
}
int main() {
	int tc;
	cin >> tc;
	int sum = 0;
	vector<pair<int, int>> amount(8001);
	vector<int> arr(tc);
	int num;
	
	for (int i = 0;i < tc;i++) {
		cin >> num;
		sum += num;
		arr[i] = num;
		++amount[num + 4000].first;
		amount[num + 4000].second = num;
	}
	sort(amount.begin(), amount.end(), compare);
	sort(arr.begin(), arr.end(), compare2);
	int first = round((double)sum / tc);
	cout << first << "\n";
	cout << arr[tc / 2] << "\n";

	
	int max_index = 0;
	for (int i = 0;i < tc-1;i++) {
		if (amount[i].first == amount[i + 1].first) ++max_index;
		else break;
	}
	if (max_index >= 1) {
		vector<int> result(max_index + 1);
		for (int i = 0;i <= max_index;i++) {
			result[i] = amount[i].second;
		}
		sort(result.begin(), result.end(), compare2);
		cout << result[max_index - 1];
	}
	else cout << amount[0].second;
	cout << "\n";
	cout << (arr[0] - arr[tc - 1]);
}