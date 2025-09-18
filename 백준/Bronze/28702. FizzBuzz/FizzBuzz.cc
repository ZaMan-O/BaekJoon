#include <iostream>
#include <string>
#include <vector>
#include <utility>
using namespace std;
int main() {
	vector<string> str(3);
	pair<int, int> index;
	for (int i = 0;i < 3;i++) {
		cin >> str[i];
		if (!(str[i] == "Fizz" || str[i] == "Buzz" || str[i] == "FizzBuzz")) {
			index.first = 3 - i;
			index.second = stoi(str[i]);
		}
	}
	int sum = index.second + index.first;
	if (sum % 3 == 0 && sum % 5 == 0) cout << "FizzBuzz";
	else if (sum % 3 == 0) cout << "Fizz";
	else if (sum % 5 == 0) cout << "Buzz";
	else cout << sum;
}