#include <iostream>
#include <vector>
using namespace std;

int main() {
	int front = 0, rear = 0;
	int max;
	cin >> max;
	++max;
	vector<int> queue(max);
	for (int i = 1;i < max;i++) {
		queue[i] = i;
	}
	rear = max - 1;
	while ((front + 1) % max != rear) {
		front = (front + 2) % max;
		rear = (++rear) % max;
		queue[rear] = queue[front];
	}
	cout << queue[(++front) % max];
}