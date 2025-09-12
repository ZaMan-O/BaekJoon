#include <iostream>
#include <vector>
#include <climits>
using namespace std;

int main() {
	int width, height;
	int min_paint = INT_MAX;
	int num;

	cin >> height >> width;
	vector<string> chess_phan(height);
	for (int i = 0;i < height;i++) {
		cin >> chess_phan[i];
	}

	for (int i = 0;i <= height - 8;i++) {
		for (int ii = 0;ii <= width - 8;ii++) {
			int now_paint = 0;

			
			for (int iii = 0;iii < 64;iii++) {
				num = iii / 8 + iii % 8;
				if (num % 2 == 0 && chess_phan[iii / 8 + i][iii % 8 + ii] != 'W') ++now_paint;
				else if (num % 2 == 1 && chess_phan[iii / 8 + i][iii % 8 + ii] != 'B') ++now_paint;
			}
			min_paint = now_paint < min_paint ? now_paint : min_paint;

			now_paint = 0;
			for (int iii = 0;iii < 64;iii++) {
				num = iii / 8 + iii % 8;
				if (num % 2 == 0 && chess_phan[iii / 8 + i][iii % 8 + ii] != 'B') ++now_paint;
				else if (num % 2 == 1 && chess_phan[iii / 8 + i][iii % 8 + ii] != 'W') ++now_paint;
			}
			min_paint = now_paint < min_paint ? now_paint : min_paint;
		}
	}
	cout << min_paint;
}