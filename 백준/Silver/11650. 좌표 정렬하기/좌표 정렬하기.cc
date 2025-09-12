#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

struct pos {
	int x;
	int y;
};

bool compare(pos a, pos b) {
	if (a.x == b.x) return a.y < b.y;
	else return a.x < b.x;
}

int main() {
	int tc;
	cin >> tc;
	vector<pos> jum(tc);
	for (int i = 0;i < tc;i++) {
		cin >> jum[i].x >> jum[i].y;
	}
	sort(jum.begin(), jum.end(), compare);
	for (int i = 0;i < tc;i++) {
		cout << jum[i].x << " " << jum[i].y << "\n";
	}
}