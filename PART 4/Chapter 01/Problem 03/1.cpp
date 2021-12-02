#include <cstdio>
#include <deque>

using namespace std;

const int dy[4] = {0, 1, 0, -1};
const int dx[4] = {1, 0, -1, 0};

struct coord {
    int y;
    int x;
};

int N, K, L, board[105][105], dir[10005], d;
deque<coord> dq;

bool isValidYx(int y, int x) {
    return 0 < y && y <= N && 0 < x && x <= N;
}

bool isCollideWithSelf(int y, int x) {
    for (auto cell: dq)
        if (y == cell.y && x == cell.x)
            return true;

    return false;
}

int main() {
    dq.emplace_back(coord{1, 1});

    scanf("%d%d", &N, &K);
    int yy, xx;
    for (int i = 0; i < K; ++i) {
        scanf("%d %d", &yy, &xx);
        board[yy][xx] = 1;
    }

    scanf("%d", &L);
    int tt;
    char dd;
    for (int i = 0; i < L; ++i) {
        scanf("%d %c", &tt, &dd);
        dir[tt] = dd;
    }

    int sec;
    for (sec = 1;; ++sec) {
        int ny = dq.front().y + dy[d];
        int nx = dq.front().x + dx[d];

        if (!isValidYx(ny, nx))
            break;

        if (isCollideWithSelf(ny, nx))
            break;

        dq.emplace_front(coord{ny, nx});

        if (board[ny][nx] == 1)
            board[ny][nx] = 0;
        else
            dq.pop_back();

        if (dir[sec] == 'D')
            d = (d + 1) % 4;
        else if (dir[sec] == 'L')
            d = (d + 3) % 4;
    }

    printf("%d\n", sec);

    return 0;
}