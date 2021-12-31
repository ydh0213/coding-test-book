#include <cstdio>

using namespace std;

int N, M, ans;
bool G[1001][1001], chk[1001];

void dfs(int now) {
    chk[now] = true;
    for (int next = 1; next <= N; ++next)
        if (G[now][next] && !chk[next])
            dfs(next);
}

int main() {
    scanf("%d %d", &N, &M);

    int u, v;
    for (int e = 0; e < M; ++e) {
        scanf("%d %d", &u, &v);
        G[u][v] = G[v][u]= true;
    }

    for (int i = 1; i <= N; ++i)
        if (!chk[i]) {
            ++ans;
            dfs(i);
        }

    printf("%d\n", ans);

    return 0;
}
