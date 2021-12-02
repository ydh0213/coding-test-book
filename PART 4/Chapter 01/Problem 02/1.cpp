#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

int N, arr[25][25], ans;

vector<vector<int> > rotateArr(vector<vector<int> > v) {
    vector<vector<int> > ret(N);
    for (int i = 0; i < N; i++)
        ret[i] = vector<int>(N, 0);

    for (int i = 0; i < N; i++)
        for (int j = 0; j < N; j++)
            ret[j][N - 1 - i] = v[i][j];

    return ret;
}

vector<vector<int> > mv(int dir, vector<vector<int> > v) {
    // 원하는 방향값만큼 회전시키고서 밀어주는 걸로 대신한다
    for (int i = 0; i < dir; i++)
        v = rotateArr(v);

    vector<vector<int> > ret(N);
    for (int i = 0; i < N; i++) {
        // 순서대로 나열한 후 0만 삭제
        vector<int> deletedZero = v[i];
        for (int j = N - 1; j >= 0; j--)
            if (deletedZero[j] == 0)
                deletedZero.erase(deletedZero.begin() + j);

        // 바로 옆 숫자랑 같으면 2 곱한 수를, 아니라면 그냥 자기자신 그대로
        int sz = deletedZero.size();
        for (int j = 0; j < sz; j++)
            if (j < sz - 1 && deletedZero[j] == deletedZero[j + 1]) {
                ret[i].emplace_back(deletedZero[j] * 2);
                j++;
            } else
                ret[i].emplace_back(deletedZero[j]);

        // 남은 자리는 0으로 채운다
        int rest = N - ret[i].size();
        for (int j = 0; j < rest; j++)
            ret[i].emplace_back(0);
    }

    return ret;
}

void dfs(int mvCnt, vector<vector<int> > v) {
    if (mvCnt == 5) {
        for (int i = 0; i < N; i++)
            for (int j = 0; j < N; j++)
                ans = max(ans, v[i][j]);

        return;
    }

    for (int dir = 0; dir < 4; dir++)
        dfs(mvCnt + 1, mv(dir, v));
}

int main() {
    scanf("%d", &N);
    for (int i = 0; i < N; i++)
        for (int j = 0; j < N; j++)
            scanf("%d", &arr[i][j]);

    vector<vector<int> > v(N);
    for (int i = 0; i < N; i++)
        for (int j = 0; j < N; j++)
            v[i].emplace_back(arr[i][j]);

    dfs(0, v);
    printf("%d\n", ans);

    return 0;
}