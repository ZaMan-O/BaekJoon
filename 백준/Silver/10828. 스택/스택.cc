#include <iostream>
using namespace std;

int main() {
	int tc;
	string command;

	int top = -1, total = 0;
	int stack[10000];
	int result[10000];

	cin >> tc;
	for (int i = 0;i < tc;i++) {
		cin >> command;
		if (command == "push") {
			int num;
			cin >> num;
			stack[++top] = num;
		}
		else if (command == "pop") {
			if (top == -1) {
				result[total++] = -1;
			}
			else {
				result[total++] = stack[top--];
			}
		}
		else if (command == "size") {
			result[total++] = top + 1;
		}
		else if (command == "empty") {
			if (top == -1) result[total++] = 1;
			else result[total++] = 0;
		}
		else if (command == "top") {
			if(top == -1) result[total++] = -1;
			else result[total++] = stack[top];
		}
	}
	for (int i = 0;i < total;i++) {
		cout << result[i] << "\n";
	}
}