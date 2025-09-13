#include <iostream>
using namespace std;

int front = -1, rear = -1, total = 0;
int queue[10000];
int result[10000];

int empty() {
	if (front == rear) return 1;
	else return 0;
}

void push() {
	int num;
	cin >> num;
	queue[++rear] = num;
}

int pop() {
	if (empty()) return -1;
	return queue[++front];
}

int size() {
	return rear - front;
}

int fr0nt() {
	if (empty()) return -1;
	return queue[front + 1];
}

int back() {
	if (empty()) return -1;
	return queue[rear];
}

int main() {
	int tc;
	string command;
	cin >> tc;
	for (int i = 0;i < tc;i++) {
		cin >> command;
		if (command == "push") push();
		else if (command == "pop") result[total++] = pop();
		else if (command == "size") result[total++] = size();
		else if (command == "empty") result[total++] = empty();
		else if (command == "front") result[total++] = fr0nt();
		else if (command == "back") result[total++] = back();
	}
	for (int i = 0;i < total;i++) {
		cout << result[i] << "\n";
	}
}