#include <cstdio>
#include <string>
#include <iostream>
#include <algorithm>

using namespace std;

const int dy[4] = {0, 1, 0, -1};
const int dx[4] = {1, 0, -1, 0};
int R, C, ans;
string board[20];
bool chk[26];

bool isValidCoord(int y, int x) {
    return 0 <= y && y < R && 0 <= x && x < C;
}

void recur(int y, int x, int l) {
    chk[board[y][x] - 'A'] = true;
    ans = max(ans, l);

    for (int k = 0; k < 4; ++k) {
        int ny = y + dy[k];
        int nx = x + dx[k];
        int nl = l + 1;
        if (isValidCoord(ny, nx) && !chk[board[ny][nx] - 'A'])
            recur(ny, nx, nl);
    }

    chk[board[y][x] - 'A'] = false;
}

int main() {
    scanf("%d %d", &R, &C);
    for (int i = 0; i < R; ++i)
        cin >> board[i];

    recur(0, 0, 1);

    printf("%d\n", ans);

    return 0;
}
