// C++
#include <cstdio>
#include <iostream>
#include <string>
#include <queue>

using namespace std;

const int dy[4] = {0, 1, 0, -1};
const int dx[4] = {1, 0, -1, 0};

class State {
public:
    State(int ry, int rx, int by, int bx, int m) : ry(ry), rx(rx), by(by), bx(bx), m(m) {};

    int ry, rx, by, bx, m;
};

int N, M, sry, srx, sby, sbx, oy, ox; // 시작 구슬 좌표들과 구멍 좌표
bool chk[10][10][10][10]; // 방문 체크
string board[10];

State goNext(const State &now, int k) {
    int nry = now.ry, nrx = now.rx;
    int nby = now.by, nbx = now.bx;

    for (int mv = 0; mv < 10; mv++) {
        nry += dy[k];
        nrx += dx[k];
        if (board[nry][nrx] == '#') {
            nry -= dy[k];
            nrx -= dx[k];
            break;
        } else if (board[nry][nrx] == 'O') break;
    }

    for (int mv = 0; mv < 10; mv++) {
        nby += dy[k];
        nbx += dx[k];
        if (board[nby][nbx] == '#') {
            nby -= dy[k];
            nbx -= dx[k];
            break;
        } else if (board[nby][nbx] == 'O') break;
    }

    // 구슬들이 구멍에 빠지지 않았으면서 충돌했을 경우
    if (nry == nby && nrx == nbx && (nry != oy || nrx != ox)) {
        switch (k) {
            case 0:
                if (now.rx < now.bx) --nrx;
                else --nbx;
                break;
            case 1:
                if (now.ry < now.by) --nry;
                else --nby;
                break;
            case 2:
                if (now.rx > now.bx) ++nrx;
                else ++nbx;
                break;
            case 3:
                if (now.ry > now.by) ++nry;
                else ++nby;
                break;
        }
    }

    return {nry, nrx, nby, nbx, now.m + 1};
}

int bfs() {
    queue<State> q;
    q.emplace(sry, srx, sby, sbx, 0);
    chk[sry][srx][sby][sbx] = true;
    while (!q.empty()) {
        State now = q.front();
        q.pop();

        if (now.by == oy && now.bx == ox) continue;

        if (now.ry == oy && now.rx == ox) return now.m;

        if (now.m < 10)
            for (int k = 0; k < 4; k++) {
                State ns = goNext(now, k);
                if (!chk[ns.ry][ns.rx][ns.by][ns.bx]) {
                    q.emplace(ns.ry, ns.rx, ns.by, ns.bx, ns.m);
                    chk[ns.ry][ns.rx][ns.by][ns.bx] = true;
                }
            }
    }

    return -1;
}

int main() {
    scanf("%d %d", &N, &M);
    for (int i = 0; i < N; i++) {
        cin >> board[i];
        for (int j = 0; j < M; ++j)
            if (board[i][j] == 'R') sry = i, srx = j;
            else if (board[i][j] == 'B') sby = i, sbx = j;
            else if (board[i][j] == 'O') oy = i, ox = j;
    }

    printf("%d\n", bfs());

    return 0;
}