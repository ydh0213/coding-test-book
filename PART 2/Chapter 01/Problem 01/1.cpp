#include <cstdio>
#include <vector>

using namespace std;

int main() {
    int N, K;
    scanf("%d %d", &N, &K);

    vector<int> peo;
    for (int i = 1; i < N + 1; ++i)
        peo.emplace_back(i);

    int pt = 0;
    vector<int> ans;
    for (int i = 0; i < N; ++i) {
        pt += K - 1;
        pt %= peo.size();
        ans.emplace_back(peo[pt]);
        peo.erase(peo.begin() + pt);
    }

    printf("<%d", ans[0]);

    for (int i = 1; i < N; ++i)
        printf(", %d", ans[i]);

    printf(">\n");

    return 0;
}
