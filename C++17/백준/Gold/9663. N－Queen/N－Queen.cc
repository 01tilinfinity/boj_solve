#include <cstdio>
#include <iostream>
#include <math.h>
#define MAX	15

using namespace std;

int N, total;
int col[MAX];
int total_count;

bool check(int level) {
	for (int i = 0; i < level; i++) {
		if (col[level] == col[i] || abs(col[level] - col[i]) == level - i)return false;

	}
	return true;
}

void queen(int x) {
	if (x == N) {
		total_count++;
	}
	else {
		for (int i = 0; i < N; i++) {
			col[x] = i;
			if (check(x)) queen(x + 1);
		}
	}
}

int main() {
	cin >> N;
	queen(0);
	cout << total_count;
}